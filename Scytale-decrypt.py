#!/bin/env python3
# Scytale cipher decrypt
import sys
key = int(sys.argv[1])

ciphertext = input().replace("\n", "")

ciphertext = ciphertext.upper().replace(" ", "")
length = int(len(ciphertext))

col = int(length / key)

k = 0
table = [["0" for x in range(col)] for y in range(key)]
plaintext = ""
for i in range(col):
	for j in range(key):
		table[j][i] = ciphertext[k]
		k += 1

for i in range(key):
	for j in range(col):
		plaintext += table[i][j]

print(plaintext)
