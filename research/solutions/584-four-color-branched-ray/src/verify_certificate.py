#!/usr/bin/env python3
"""Replay a semantic rational certificate without NumPy, SciPy or an optimizer."""
import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

from probability_rules import equation, nonnegative_expression, short_affine_table


def verify(data):
    if data['format_version']!=1 or data['max_ray_length']!=8 or data['max_line_length']!=10:
        raise ValueError('Unsupported certificate format or cylinder dimensions')
    affine=short_affine_table()
    coefficients=defaultdict(Q)
    offset=Q(0)

    def add(weight,expression):
        nonlocal offset
        terms,value=expression
        offset+=weight*value
        for name,coefficient in terms.items():coefficients[name]+=weight*coefficient

    for item in data['equations']:
        add(Q(item['multiplier']),equation(item,affine))
    for item in data['nonnegative_expressions']:
        weight=Q(item['multiplier'])
        if weight<0:raise ValueError('Negative multiplier for a nonnegative expression')
        add(weight,nonnegative_expression(item))
    residual={name:str(c) for name,c in coefficients.items() if c}
    if residual:
        first=next(iter(residual.items()))
        raise ValueError(f'Nonzero exact coefficient: {first}')
    margin=-offset
    if margin<=Q(0):raise ValueError('Certificate has no strictly negative constant')
    if margin!=Q(data['expected_margin']):raise ValueError('Recorded and computed margins differ')
    if margin<=Q(1,50) or Q(data['minimum_margin'])!=Q(1,50):
        raise ValueError('Advertised margin bound failed')
    return {'status':'EXACT_CERTIFICATE_REPLAY_PASSED','short_cylinders':len(affine),'equations':len(data['equations']),'nonnegative_expressions':len(data['nonnegative_expressions']),'probability_and_moment_symbols':len(coefficients),'nonzero_coefficients':0,'margin':str(margin),'margin_decimal':float(margin),'margin_strictly_greater_than':'1/50'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    started=time.monotonic()
    raw=args.certificate.read_bytes()
    report=verify(json.loads(raw))
    report['certificate_sha256']=hashlib.sha256(raw).hexdigest()
    report['seconds']=time.monotonic()-started
    if args.output:args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
