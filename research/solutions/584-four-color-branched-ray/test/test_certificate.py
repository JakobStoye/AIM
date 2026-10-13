"""Mathematical controls and deliberate-corruption checks for the verifier."""
import copy
from fractions import Fraction as Q
from functools import lru_cache
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
import probability_rules as rules
from verify_certificate import verify


@lru_cache(None)
def holroyd_liggett(word):
    if any(a==b for a,b in zip(word,word[1:])):return Q(0)
    if not word:return Q(1)
    return sum((holroyd_liggett(word[:i]+word[i+1:]) for i in range(len(word))),Q(0))/Q(2*(len(word)+1))


class MathematicalControls(unittest.TestCase):
    def test_published_line_recursion_satisfies_erasure_rules(self):
        count=0
        for descriptor in rules.descriptors(4):
            if not descriptor['rule'].startswith('line-') and descriptor['rule']!='one-site':continue
            terms,offset=rules.equation(descriptor)
            value=offset
            for name,weight in terms.items():
                kind,word=rules.parse_symbol(name)
                self.assertEqual(kind,'p')
                value+=weight*holroyd_liggett(word)
            self.assertEqual(value,0,descriptor)
            count+=1
        self.assertGreater(count,100)

    def test_star_neighbors_are_independent_uniforms(self):
        for a in range(4):
            for b in range(4):
                for ray in range(4):
                    total=sum((rules.fixed_probability('s',(a,b,root,ray)) for root in range(4)),Q(0))
                    self.assertEqual(total,Q(1,64))

    def test_star_leaf_marginal_matches_short_line(self):
        for a in range(4):
            for root in range(4):
                for ray in range(4):
                    total=sum((rules.fixed_probability('s',(a,b,root,ray)) for b in range(4)),Q(0))
                    self.assertEqual(total,rules.fixed_probability('p',(a,root,ray)))

    def test_independent_set_bounds(self):
        self.assertEqual(rules.independent_probability_bound('p:0,1,0,1'),Q(1,16))
        self.assertEqual(rules.independent_probability_bound('p:0,1,2,0,1'),Q(1,64))
        self.assertEqual(rules.independent_probability_bound('s:0,0,1,2,1'),Q(1,64))
        self.assertEqual(rules.independent_probability_bound('s:0,0,1,2,1,2'),Q(1,256))

    def test_leaf_order_is_preserved(self):
        self.assertNotEqual(rules.symbol('s',(0,1,2,0,3)),rules.symbol('s',(1,0,2,0,3)))
        self.assertEqual(rules.symbol('p',(0,1,2,0,3)),rules.symbol('p',(3,0,2,1,0)))

    def test_parameter_enclosure_entries(self):
        table=rules.short_affine_table()
        self.assertEqual(len(table),78)
        self.assertEqual(table['p:0,1,0,1,0'],(Q(-1,288),Q(1,48),Q(0)))
        self.assertEqual(table['s:0,0,1,2,1,3'],(Q(1,1152),Q(0),Q(0)))
        self.assertEqual(table['s:0,0,1,2,1'],(Q(1,256),Q(-1,96),Q(0)))
        self.assertEqual(table['s:0,0,1,2,1,2'],(Q(-1,1152),Q(0),Q(1,972)))
        self.assertEqual(table['s:0,1,2,0,2,0'],(Q(1,768),Q(0),Q(-1,972)))

    def test_invalid_graph_adjacency_is_rejected(self):
        with self.assertRaises(ValueError):
            rules.nonnegative_expression({'rule':'critical','kind':'s','word':[0,0,1,1]})

    def test_invalid_erasure_location_is_rejected(self):
        with self.assertRaises(ValueError):
            rules.equation({'rule':'line-gap','word':[0,1,0],'gap':0})


class CertificateControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'certificate/farkas.json').read_text())

    def test_full_exact_certificate(self):
        report=verify(self.data)
        self.assertEqual(report['nonzero_coefficients'],0)
        self.assertGreater(Q(report['margin']),Q(1,50))

    def test_negative_inequality_multiplier_is_rejected(self):
        data=copy.deepcopy(self.data)
        data['nonnegative_expressions'][0]['multiplier']='-1'
        with self.assertRaisesRegex(ValueError,'Negative multiplier'):verify(data)

    def test_changed_equality_weight_is_rejected(self):
        data=copy.deepcopy(self.data)
        data['equations'][0]['multiplier']=str(Q(data['equations'][0]['multiplier'])+1)
        with self.assertRaisesRegex(ValueError,'Nonzero exact coefficient'):verify(data)

    def test_fabricated_margin_is_rejected(self):
        data=copy.deepcopy(self.data)
        data['expected_margin']='1'
        with self.assertRaisesRegex(ValueError,'margins differ'):verify(data)


if __name__=='__main__':unittest.main()
