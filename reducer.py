#!/usr/bin/python
# coding=utf-8
import sys
from collections import defaultdict


def reduce():
	data = defaultdict(set)	
	for pipe in sys.stdin:
		line = pipe.strip('\n').split('\t')
		machine = line[0]
		time = int(line[1])
		#add the key to the dictionary, adding or incrementing the time value
		data[machine].add(time + int(data.get(machine))
	for key in data:
		print 'Macchina 'key + ': ' + data.get(key) + ' minuti'

if __name__ == '__main__':
	reduce()