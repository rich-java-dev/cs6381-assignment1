import sys
import argparse
from netutils import proxy

parser = argparse.ArgumentParser()
parser.add_argument("--xin", "--in_bound", default="5555")
parser.add_argument("--xout", "--out_bound", default="5556")
args = parser.parse_args()

in_bound = args.xin
out_bound = args.xout

proxy(in_bound, out_bound)
