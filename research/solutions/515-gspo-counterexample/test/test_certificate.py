"""Small controls for the independent definition-based certificate checker."""
from fractions import Fraction
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'));sys.path.insert(0,str(ROOT/'scripts'))
from dmag_reference import Graph,determinant,gaussian_dependences
from verify_certificate import verify


class CertificateControls(unittest.TestCase):
    def test_empty_and_pivoted_determinants(self):
        self.assertEqual(determinant([]),1)
        self.assertEqual(determinant([[0,2],[3,4]]),-6)
        self.assertEqual(determinant([[1,2],[2,4]]),0)
        self.assertEqual(determinant([[Fraction(1,2),1],[1,3]]),Fraction(1,2))

    def test_collider_conditioning_and_descendant(self):
        collider=Graph.from_edges(4,[(0,1),(2,1),(1,3)])
        self.assertFalse(collider.mconnected(0,2,0))
        self.assertTrue(collider.mconnected(0,2,1<<1))
        self.assertTrue(collider.mconnected(0,2,1<<3))
        chain=Graph.from_edges(3,[(0,1),(1,2)])
        self.assertTrue(chain.mconnected(0,2,0))
        self.assertFalse(chain.mconnected(0,2,1<<1))

    def test_nonmaximal_ancestral_graph(self):
        graph=Graph.from_edges(4,[(1,3),(2,0)],[(0,1),(1,2),(2,3)])
        self.assertTrue(graph.ancestral())
        self.assertFalse(graph.maximal())
        closure=graph.closure()
        self.assertEqual(closure.state(0,3),3)
        self.assertEqual(closure.signature(),graph.signature())

    def test_gaussian_fork_and_conditional_independence(self):
        covariance=[[1,1,1],[1,2,1],[1,1,2]]
        dep=gaussian_dependences(covariance)
        self.assertTrue(dep[2][0])
        self.assertFalse(dep[2][1])

    def test_full_certificate(self):
        self.assertEqual(verify()['status'],'PASS')

    def test_reject_changed_covariance(self):
        data=json.loads((ROOT/'numerical_case/counterexample.json').read_text())
        data['covariance'][0][5]=1;data['covariance'][5][0]=1
        with tempfile.TemporaryDirectory(dir=ROOT/'numerical_case') as directory:
            p=Path(directory)/'invalid.json';p.write_text(json.dumps(data))
            with self.assertRaises(AssertionError):verify(p)


if __name__=='__main__':unittest.main()
