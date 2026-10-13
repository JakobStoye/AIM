"""Exact finite probability identities for a symmetric four-color branched ray.

The verifier uses only the Python standard library. Probabilities are for
specified color words, never orbit masses. Line reflection is allowed; a
branched word retains the ordered leaves and is never reflected.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache

COLORS = range(4)
MOMENTS = ('alpha', 'gamma', 'alpha_square', 'alpha_gamma')


def renamed(word):
    names = {}
    return tuple(names.setdefault(c, len(names)) for c in word)


def line_name(word):
    return min(renamed(word), renamed(tuple(reversed(word))))


def proper_line(word):
    return all(x != y for x, y in zip(word, word[1:]))


def proper_branch(word):
    a, b, root, *ray = word
    return a != root and b != root and proper_line((root, *ray))


def symbol(kind, word):
    if kind == 'p':
        return 'p:' + ','.join(map(str, line_name(tuple(word))))
    if kind == 's':
        return 's:' + ','.join(map(str, renamed(tuple(word))))
    if kind == 'm' and len(word) == 1 and word[0] in MOMENTS:
        return 'm:' + word[0]
    raise ValueError('Invalid probability or moment symbol')


def parse_symbol(name):
    kind, data = name.split(':')
    if kind == 'm':
        if data not in MOMENTS:
            raise ValueError('Unknown moment')
        return kind, (data,)
    word = tuple(int(c) for c in data.split(','))
    if not word or any(c not in COLORS for c in word):
        raise ValueError('Invalid color word')
    if kind == 'p' and not proper_line(word):
        raise ValueError('Improper line word')
    if kind == 's' and (len(word) < 4 or not proper_branch(word)):
        raise ValueError('Improper branched word')
    if symbol(kind, word) != name:
        raise ValueError('Noncanonical symbol')
    return kind, word


def empty():
    return ({}, Q(0))


def constant(value):
    return ({}, Q(value))


def atom(name):
    return ({name: Q(1)}, Q(0))


def combine(items):
    coefficients = defaultdict(Q)
    offset = Q(0)
    for weight, (terms, value) in items:
        offset += weight * value
        for name, coefficient in terms.items():
            coefficients[name] += weight * coefficient
    return ({name: c for name, c in coefficients.items() if c}, offset)


def probability(kind, word):
    word = tuple(word)
    if kind == 'p':
        if not word:
            return constant(1)
        if not proper_line(word):
            return empty()
    elif kind == 's':
        if not proper_branch(word):
            return empty()
        if len(word) == 3:
            a, b, root = word
            return probability('p', (a, root, b))
    else:
        raise ValueError('Unknown geometry')
    return atom(symbol(kind, word))


def fixed_probability(kind, word):
    word = tuple(word)
    if kind == 's':
        if not proper_branch(word):
            return Q(0)
        if len(word) == 3:
            a, b, root = word
            return fixed_probability('p', (a, root, b))
        if len(word) == 4:
            a, b, _, first = word
            return Q(1, 64 * (4 - len({a, b, first})))
        return None
    if not proper_line(word):
        return Q(0)
    if not word:
        return Q(1)
    if len(word) == 1:
        return Q(1, 4)
    if len(word) == 2:
        return Q(1, 12)
    if len(word) == 3:
        return Q(1, 48) if word[0] == word[2] else Q(1, 32)
    return None


def patterns(length, branch=False):
    def visit(prefix, maximum):
        if len(prefix) == length:
            if (proper_branch(prefix) if branch else proper_line(prefix)):
                yield prefix
            return
        for color in range(min(3, maximum + 1) + 1):
            yield from visit(prefix + (color,), max(maximum, color))
    result = set(visit((0,), 0))
    if not branch:
        result = {line_name(w) for w in result}
    return sorted(result)


def descriptors(ray_length):
    yield {'rule': 'one-site'}
    for length in range(1, ray_length + 3):
        for word in patterns(length):
            if length > 1:
                yield {'rule': 'line-marginal', 'word': word}
            for gap in range(1, length - 1):
                yield {'rule': 'line-gap', 'word': word, 'gap': gap}
    for length in range(1, ray_length + 1):
        for word in patterns(length + 3, branch=True):
            for rule in ('star-marginal', 'path-a', 'path-b', 'root-gap'):
                yield {'rule': rule, 'word': word}
            for gap in range(length):
                yield {'rule': 'star-gap', 'word': word, 'gap': gap}


def affine_product(left, right, affine):
    def coordinates(expression):
        terms, offset = expression
        if not terms:
            return offset, Q(0), Q(0)
        if len(terms) != 1 or offset:
            raise ValueError('Non-atomic product factor')
        name, weight = next(iter(terms.items()))
        return tuple(weight * c for c in affine[name])
    c, a, g = coordinates(left)
    d, b, h = coordinates(right)
    if g * h:
        raise ValueError('A gamma-square term is outside this certificate')
    values = (a*d+c*b, g*d+c*h, a*b, a*h+g*b)
    return ({'m:'+name: value for name, value in zip(MOMENTS, values) if value}, c*d)


def product(left_kind, left_word, right_kind, right_word, affine):
    left = probability(left_kind, left_word)
    right = probability(right_kind, right_word)
    lv = fixed_probability(left_kind, left_word)
    rv = fixed_probability(right_kind, right_word)
    if lv is not None:
        return combine([(lv, right)])
    if rv is not None:
        return combine([(rv, left)])
    if affine is None:
        raise ValueError('Unresolved product in the low-order system')
    return affine_product(left, right, affine)


def equation(descriptor, affine=None):
    rule = descriptor['rule']
    if rule == 'one-site':
        return combine([(1, probability('p', (0,))), (-1, constant(Q(1,4)))])
    if rule == 'alpha-alias':
        return combine([(1,atom('m:alpha')),(-48,probability('p',(0,1,0,1)))])
    if rule == 'gamma-alias':
        return combine([(1,atom('m:gamma')),(-972,probability('s',(0,1,2,1,3,1)))])
    word = tuple(descriptor['word'])
    if any(c not in COLORS for c in word):
        raise ValueError('Invalid color')
    if rule.startswith('line-'):
        if not 2 <= len(word) <= 10 or not proper_line(word):
            raise ValueError('Invalid line descriptor')
        if rule == 'line-marginal':
            return combine([(1,probability('p',word[:-1]+(c,))) for c in COLORS] + [(-1,probability('p',word[:-1]))])
        if rule == 'line-gap':
            gap = descriptor['gap']
            if not 1 <= gap < len(word)-1:
                raise ValueError('Invalid line gap')
            left,right=word[:gap],word[gap+1:]
            return combine([(1,probability('p',left+(c,)+right)) for c in COLORS]+[(-1,product('p',left,'p',right,affine))])
        raise ValueError('Unknown line rule')
    if not 4 <= len(word) <= 11 or not proper_branch(word):
        raise ValueError('Invalid branched descriptor')
    a,b,root,*ray_list=word
    ray=tuple(ray_list)
    if rule=='star-marginal':
        return combine([(1,probability('s',word[:-1]+(c,))) for c in COLORS]+[(-1,probability('s',word[:-1]))])
    if rule=='path-a':
        return combine([(1,probability('s',(a,c,root)+ray)) for c in COLORS]+[(-1,probability('p',(a,root)+ray))])
    if rule=='path-b':
        return combine([(1,probability('s',(c,b,root)+ray)) for c in COLORS]+[(-1,probability('p',(b,root)+ray))])
    if rule=='root-gap':
        return combine([(1,probability('s',(a,b,c)+ray)) for c in COLORS]+[(-Q(1,16),probability('p',ray))])
    if rule=='star-gap':
        gap=descriptor['gap']
        if not 0 <= gap < len(ray):
            raise ValueError('Invalid ray gap')
        prefix,suffix=word[:3+gap],ray[gap+1:]
        return combine([(1,probability('s',prefix+(c,)+suffix)) for c in COLORS]+[(-1,product('s',prefix,'p',suffix,affine))])
    raise ValueError('Unknown equality rule')


@lru_cache(None)
def short_affine_table():
    """Derive all short cylinders using exact sparse Gaussian elimination."""
    names=[symbol('p',w) for k in range(1,6) for w in patterns(k)]
    names += [symbol('s',w) for k in range(1,4) for w in patterns(k+3,branch=True)]
    positions={name:i for i,name in enumerate(names)}
    rows={}
    for desc in [*descriptors(3),{'rule':'alpha-alias'},{'rule':'gamma-alias'}]:
        terms,offset=equation(desc)
        if any(name not in positions and name not in ('m:alpha','m:gamma') for name in terms):
            raise ValueError('Unexpected symbol in the short-cylinder system')
        row={positions[name]:c for name,c in terms.items() if name in positions}
        # Store the right side in coordinates (constant, alpha, gamma).
        rhs=[-offset,-terms.get('m:alpha',Q(0)),-terms.get('m:gamma',Q(0))]
        while row:
            pivot=min(row)
            if pivot not in rows:
                value=row[pivot]
                rows[pivot]=({i:c/value for i,c in row.items()},[c/value for c in rhs])
                break
            known,known_rhs=rows[pivot]
            weight=row[pivot]
            for i,c in known.items():
                row[i]=row.get(i,Q(0))-weight*c
                if not row[i]:del row[i]
            rhs=[c-weight*d for c,d in zip(rhs,known_rhs)]
        else:
            if any(rhs):raise ValueError('Inconsistent short-cylinder identities')
    if len(rows)!=len(names):raise ValueError('Short-cylinder aliases do not give full rank')
    values={}
    for pivot in reversed(range(len(names))):
        row,rhs=rows[pivot]
        for i,weight in row.items():
            if i==pivot:continue
            rhs=[c-weight*d for c,d in zip(rhs,values[i])]
        values[pivot]=tuple(rhs)
    table={name:values[i] for i,name in enumerate(names)}
    # Check every original short identity after substitution, including rows
    # not selected as Gaussian pivots.
    for desc in [*descriptors(3),{'rule':'alpha-alias'},{'rule':'gamma-alias'}]:
        terms,offset=equation(desc)
        check=[offset,terms.get('m:alpha',Q(0)),terms.get('m:gamma',Q(0))]
        for name,weight in terms.items():
            if name in table:check=[c+weight*d for c,d in zip(check,table[name])]
        if any(check):raise ValueError('Failed exact short-table substitution')
    return table


def independent_probability_bound(name):
    kind,word=parse_symbol(name)
    if kind=='p':return Q(1,4**((len(word)+1)//2))
    if kind=='s':return Q(1,4**(2+(len(word)-2)//2))
    bounds={'alpha':Q(5,24),'gamma':Q(81,64),'alpha_square':Q(25,576),'alpha_gamma':Q(135,512)}
    return bounds[word[0]]


def nonnegative_expression(descriptor):
    rule=descriptor['rule']
    if rule=='critical':
        kind,word=descriptor['kind'],tuple(descriptor['word'])
        if kind not in ('p','s') or not word:
            raise ValueError('Invalid critical prefix')
        parse_symbol(symbol(kind,word))
        return combine([(Q(1,2),probability(kind,word[:-1])),(-1,probability(kind,word))])
    if rule=='square-tangent':
        center=Q(descriptor['center'])
        return combine([(1,atom('m:alpha_square')),(-2*center,atom('m:alpha')),(center*center,constant(1))])
    if rule in ('nonnegative','independent-upper'):
        name=descriptor['symbol']
        parse_symbol(name)
        if rule=='nonnegative':return atom(name)
        return combine([(1,constant(independent_probability_bound(name))),(-1,atom(name))])
    raise ValueError('Unknown nonnegative rule')
