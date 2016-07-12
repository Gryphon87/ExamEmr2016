#!/usr/bin/python
# coding=utf-8
import sys
from collections import defaultdict


def reduce():
	my_dict = defaultdict(set)	
	for pipe in sys.stdin:
		line = pipe.strip()
		machine = line.split('\t')[0]
		time = line.split('\t')[1]
		
		#add the key to the dictionary, adding or incrementing the time value
		my_dict[machine].add(time + my_dict[machine])

	for key in my_dict:
		print key + '\t' + s

if __name__ == '__main__':
	reduce()