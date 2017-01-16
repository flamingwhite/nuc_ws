#!/usr/bin/env python3
import subprocess
import sys

from functools import reduce

def print_top_history():
	n = 20
	def combine(acc, cur):
		acc[cur] = acc.get(cur, 0) + 1
		return acc

	cmds = [' '.join(li.split()[1:]) for li in sys.stdin.readlines()]
	print('{} history items found'.format(len(cmds)))
	for cmd, ct in sorted(reduce(combine, cmds, {}).items(), key=lambda c: -c[1])[:n]:
		print('{} <= {}'.format(ct, cmd))

if __name__ == '__main__':
	print_top_history()
