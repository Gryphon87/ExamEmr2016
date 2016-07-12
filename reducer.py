#!/usr/bin/python
import sys
from collections import defaultdict


def reduce():
	results = defaultdict(int)	
	for pipe in sys.stdin:
		line = pipe.strip('\n').split('\t')
		machine = line[0]
		time = int(line[1])
		#add the key to the dictionary, adding or incrementing the time value
		results[machine].add(time + results.get(machine))

	for key in results:
		print('Macchina ' + key + ': ' + str(results[key]))

if __name__ == '__main__':
	reduce()