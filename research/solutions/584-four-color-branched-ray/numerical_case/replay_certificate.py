#!/usr/bin/env python3
"""Reproduce the proof-critical exact arithmetic case from public inputs."""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from verify_certificate import main

if __name__=='__main__':
    sys.argv=[sys.argv[0],str(ROOT/'certificate/farkas.json')]+sys.argv[1:]
    main()
