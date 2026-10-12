"""Verify the explicit counterexample with exact arithmetic and path definitions.

Run from any directory with Python 3. No third-party packages are required.
This checks a finite mathematical certificate, not a Lean formalization.
"""
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from dmag_reference import Graph,determinant,gaussian_dependences,poset_map


def verify(path=ROOT/'numerical_case/counterexample.json'):
    if not __debug__:
        raise RuntimeError('Run this verifier without Python optimization (-O or -OO).')
    data=json.loads(Path(path).read_text())
    covariance=data['covariance'];L=data['noise_transform'];n=len(covariance)
    assert n==6 and determinant(L)==1
    assert covariance==[[sum(L[i][k]*L[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    assert all(determinant([row[:k] for row in covariance[:k]])>0 for k in range(1,n+1))
    dep=gaussian_dependences(covariance)
    truth=Graph.from_key(n,data['truth_key'])
    assert truth.ancestral() and truth.maximal()
    extra=[];queries=0
    for k,(a,b) in enumerate(truth.pairs):
        table=data['minor_tables'][k]
        assert table['pair']==[a+1,b+1]
        others=[v for v in range(n) if v not in(a,b)]
        assert table['conditioning_vertices']==[v+1 for v in others]
        graph_zero=[]
        protected=bool(truth.state(a,b)) or any(v not in(a,b) and truth.state(a,v) and truth.state(b,v) for v in range(n))
        for code in range(16):
            cond=[v for j,v in enumerate(others) if code&(1<<j)]
            mask=sum(1<<v for v in cond)
            num=determinant([[covariance[i][j] for j in [b]+cond] for i in [a]+cond])
            assert num==table['numerators'][code]
            separated=not truth.mconnected(a,b,mask)
            if separated:
                assert not dep[k][mask],('Markov',a,b,mask)
                graph_zero.append(code)
            elif not dep[k][mask]:
                extra.append([a+1,b+1,cond])
                assert not protected,('restricted faithfulness',a,b,mask)
            queries+=1
        assert graph_zero==table['graph_separations']
    assert extra==[[1,6,[]]],extra
    keys=data['component_keys'];minimum=data['minimum_edges'];higher=data['component_edge_count']
    assert minimum==6 and higher==8
    images={item['key']:item for item in data['poset_map_tables']}
    for key in [data['truth_key']]+keys:
        g=Graph.from_key(n,key);anc=g.ancestors()
        assert g.ancestral() and g.maximal()
        assert poset_map(n,anc,dep).key()==key,('two A passes and closure',key)
        assert anc==images[key]['ancestors']
        for k,(a,b) in enumerate(g.pairs):
            entry=images[key]['adjacency_table'][k]
            mask=(anc[a]|anc[b])&~((1<<a)|(1<<b))
            cond=[v for v in range(n) if mask&(1<<v)]
            assert entry['pair']==[a+1,b+1] and entry['conditioning']==[v+1 for v in cond]
            num=determinant([[covariance[i][j] for j in [b]+cond] for i in [a]+cond])
            den=determinant([[covariance[i][j] for j in cond] for i in cond])
            assert str(num/den)==entry['conditional_covariance'] and g.states[k]==entry['edge_state']
        if key==data['truth_key']:
            assert sum(bool(s) for s in g.states)==minimum
            for k,s in enumerate(g.states):
                if s:
                    assert all(dep[k][mask] for mask in g.query_masks(*g.pairs[k]))
            continue
        assert sum(bool(s) for s in g.states)==higher
        neighbors=list(g.legitimate_neighbors())
        mapped={poset_map(n,h.ancestors(),dep).key() for h in neighbors}
        assert mapped==set(data['successors'][str(key)])
        assert mapped<=set(keys),('component not closed',key,mapped)
    return {'status':'PASS','gaussian_queries':queries,'extra_independences':extra,'component_vertices':len(keys),'component_edges':higher,'global_minimum_edges':minimum,'exact_successors':data['successors'],'checks':['positive definite Gaussian covariance','all restricted-faithfulness and Markov clauses','all four original two-pass/closure fixed points','all legitimate changes via exhaustive separation signatures','closed reachable component and smaller original-search vertex']}


if __name__=='__main__':
    receipt=verify(Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'numerical_case/counterexample.json')
    print(json.dumps(receipt,indent=2))
