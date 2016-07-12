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
	for key in my_dict:
		print('Macchina ' + key + ': ' + str(my_dict[key]))

if __name__ == '__main__':
	reduce()