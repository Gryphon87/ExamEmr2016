#!/usr/bin/python
import sys
def map():
	for line in sys.stdin:
		data = line.strip('\n').split(';')
		machine_id = data[2]
		time = data[3]
		print machine_id + '\t' + time
						
if __name__ == '__main__':
	map()