#!/bin/env python3
import random
import string
import sys

alphabet = list(string.ascii_lowercase)
num = int(sys.argv[1])	# generate how many key file
size = int(sys.argv[2])	# the length of the key

for i in range(num):
	key = ""
	for j in range(size):
		index = random.randint(0, 25)
		key += alphabet[index].upper()
	with open("key68496.txt", 'w') as fout:
		for k in range(size):
			'''
			if k % 5 == 0 and k != 0:
				fout.write(" ")
			if k % 40 == 0 and k != 0:
				fout.write("\n")
			'''
			fout.write(str(key[k]))
