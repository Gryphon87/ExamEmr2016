#!/usr/bin/python
import sys
from collections import defaultdict


def reduce():
	my_dict = defaultdict(set)	
	for pipe in sys.stdin:
		line = pipe.strip('\n').split('\t')
		machine = line[0]
		time = int(line[1])
		#add the key to the dictionary, adding or incrementing the time value
		my_dict[machine].add(time + int(my_dict.get(machine))
	print my_dict

if __name__ == '__main__':
	reduce()