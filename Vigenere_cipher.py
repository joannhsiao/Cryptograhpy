import sys

key = sys.argv[1]
table = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
n = input("encrypt or decrypt?(e/d)")
if n == "e":
	plain = input("plaintext: ")
	if len(key) != len(plain):
		index = 0
		for i in range(0, len(plain)-len(key)):
			key += key[index]
			if index == len(key):
				index = 0
			else:
				index += 1
	cipher = ""
	for j in range(len(plain)):
		value = (table[key[j]] + table[plain[j]]) % 26
		cipher += list(table.keys())[list(table.values()).index(value)]
	print("ciphertext: ", cipher)
else:
	cipher = input("ciphertext: ")
	if len(key) != len(cipher):
		index = 0
		for i in range(0, len(cipher)-len(key)):
			key += key[index]
			if index == len(key):
				index = 0
			else:
				index += 1
	plain = ""
	for j in range(len(cipher)):
		value = (table[cipher[j]] - table[key[j]] + 26) % 26
		plain += list(table.keys())[list(table.values()).index(value)]
	print("plaintext: ", plain)