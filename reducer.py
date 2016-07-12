#!/usr/bin/python
import sys
from collections import defaultdict


def reduce():
	current = None
	ctime = 0
	for pipe in sys.stdin:
		line = pipe.strip('\n').split('\t')
		machine = line[0]
		time = int(line[1])
		# the first iteration will override the current var to the machine var
		if (current == None):
			current = machine
		# if the machine doesn't change it will add the time
		if (machine == current):
			ctime += time
		else:
			#print the previous values and reset the current ones
			print ('Machine ' + current + ': ' + ctime)
			current = machine
			ctime = time

if __name__ == '__main__':
	reduce()