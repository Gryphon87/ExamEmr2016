#!/usr/bin/python
# coding=utf-8
import sys
from collections import defaultdict


def reduce():
	results = defaultdict(set)	
	for pipe in sys.stdin:
		line = pipe.strip()
		machine = line.split('\t')[0]
		time = int(line.split('\t')[1])
		
		#add the key to the dictionary, adding or incrementing the time value
		results[machine].add(time + int(results.get(machine))

	for key in results:
		print key + '\t' + s

if __name__ == '__main__':
	reduce()