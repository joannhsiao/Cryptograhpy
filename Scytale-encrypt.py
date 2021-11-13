#!/bin/env python3
# Scytale cipher encrypt
import sys
import string
import random
import math
key = int(sys.argv[1])

plaintext = ""
while True:
    try:
        n = input().replace("\n", "")
        plaintext += n
    except EOFError:
        break

plaintext = plaintext.upper().replace(" ", "")
length = int(len(plaintext))

col = int(math.ceil(length / key))

if length < col*key:
    for i in range(int(col*key - length)):
        plaintext += random.choice(string.ascii_letters).upper()
length = int(len(plaintext))

k = 0
table = [["0" for x in range(col)] for y in range(key)]
ciphertext = ""
for i in range(0, key):
	for j in range(0, col):
		table[i][j] = plaintext[k]
		k += 1

for i in range(0, col):
	for j in range(0, key):
		ciphertext += table[j][i]

print("ciphertext: ", ciphertext)
