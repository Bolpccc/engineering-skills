import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from governance import active_calls, catalog_errors, compatible

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = {'skills': [{'name':'alpha-skill','path':'alpha-skill','depends_on':[], 'routes_to':['beta-skill']}, {'name':'beta-skill','path':'beta-skill','depends_on':[], 'routes_to':['alpha-skill']}], 'external_skills':[]}
        for e in self.data['skills']:
            p=self.root/e['path'];p.mkdir();(p/'SKILL.md').write_text('---\nname: '+e['name']+'\n---\n')
    def test_route_round_trip(self):
        self.assertEqual(catalog_errors(self.root,self.data), [])
    def test_dependency_cycle(self):
        for e in self.data['skills']: e['depends_on']=e['routes_to']
        self.assertTrue(any('cycle' in e for e in catalog_errors(self.root,self.data)))
    def test_unknown_route(self):
        self.data['skills'][0]['routes_to']=['missing-skill']
        self.assertTrue(any('undeclared' in e for e in catalog_errors(self.root,self.data)))
    def test_unlisted_invocation(self):
        (self.root/'alpha-skill/SKILL.md').write_text('Load `$missing-skill`.\n')
        self.assertTrue(any('unlisted active' in e for e in catalog_errors(self.root,self.data)))
    def test_reference_invocation(self):
        (self.root/'alpha-skill/SKILL.md').write_text('[Protocol](protocol.md)\n')
        (self.root/'alpha-skill/protocol.md').write_text('加载 `missing-skill`。')
        self.assertTrue(any('unlisted active' in e for e in catalog_errors(self.root,self.data)))
    def test_examples_and_prohibitions(self):
        self.assertEqual(active_calls('Do not invoke `$old-skill`.\n```\nload `$old-skill`\n```\n## Example\nload `$old-skill`\n## Route\nLoad `$real-skill`.'), {'real-skill'})
    def test_missing_install(self):
        self.assertTrue(any('missing installed' in e for e in catalog_errors(self.root,self.data,self.root/'empty')))
    def test_version_bounds(self):
        for version,result in [('1.0.0',True),('1.9.9',True),('0.9.9',False),('2.0.0',False),('unknown',False)]:
            self.assertEqual(compatible(version,'>=1.0.0,<2.0.0'),result)
    def test_installed_version(self):
        self.data['external_skills']=['bridge-skill'];self.data['external_version_constraints']={'bridge-skill':'>=1.0.0,<2.0.0'};self.data['skills'][0]['depends_on']=['bridge-skill']
        p=self.root/'bridge-skill';p.mkdir()
        for version,valid in [('1.0.1',True),('2.0.0',False)]:
            (p/'SKILL.md').write_text('---\nname: bridge-skill\nmetadata:\n  version: '+version+'\n---\n')
            self.assertEqual(catalog_errors(self.root,self.data,self.root)==[],valid)
    def test_invalid_constraint(self):
        self.data['external_version_constraints']={'x-skill':'latest'}
        self.assertTrue(any('invalid constraint' in e for e in catalog_errors(self.root,self.data)))

if __name__ == '__main__': unittest.main()
