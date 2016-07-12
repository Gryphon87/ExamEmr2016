#!/usr/bin/python
# coding=utf-8
import sys
from collections import defaultdict


def reduce():
	dataset = defaultdict(set)	
	for pipe in sys.stdin:
		line = pipe.strip('\n').split('\t')
		machine = line[0]
		time = int(line[1])
		#add the key to the dictionary, adding or incrementing the time value
		dataset[machine].add(time + int(dataset.get(machine))

	for key in dataset:
		print 'Macchina 'key + ': ' + dataset.get(key) + ' minuti'

if __name__ == '__main__':
	reduce()