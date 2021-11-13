#! /bin/env python3
# playfair cipher encrypt
# rule: add X in the end of the plaintext if the lenghth is odd
import sys
import string
len_argv = len(sys.argv)

key = ""
for i in range(1, len_argv):
	key += sys.argv[i]
key = key.translate(str.maketrans('', '', string.punctuation)).upper()
key = key.replace(" ", "")
len_key = len(key)

# replace J/I with I/J
for i in range(len_key):
	if key[i] == "J":
		key[i] = "I"

key = ''.join(sorted(set(key), key=key.index))

# create a 5x5 table (replace IJ with II)
table = "ABCDEFGHIIKLMNOPQRSTUVWXYZ"
for i in range(0, len(table)):
    if table[i] not in key:
        key += str(table[i])

maze = [[0 for x in range(5)] for y in range(5)]
index = 0
for i in range(0, 5):
    for j in range(0, 5):
        maze[i][j] = key[index]
        index += 1

#ciphertext = input("ciphertext: ")
ciphertext = ""
while True:
    try:
        n = input().replace("\n", "")
        ciphertext += n
    except EOFError:
        break
ciphertext = ciphertext.upper().replace(" ", "")

def separate(ciphertext):
    matrix = []
    i = 0
    while i < len(ciphertext):
        matrix.append([ciphertext[i], ciphertext[i + 1]])
        i += 2
    return matrix

def findlocation(c):
    location = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(maze):
        for k, l in enumerate(j):
            if c == l:
                location.append(i)
                location.append(k)
    return location

matrix = separate(ciphertext)
i = 0
plaintext = ""
while i < len(matrix):
    loc_1 = findlocation(matrix[i][0])
    loc_2 = findlocation(matrix[i][1])
    if loc_1[1] == loc_2[1]:	# same row
        plaintext += (maze[(loc_1[0]-1+5)%5][loc_1[1]] + maze[(loc_2[0]-1+5)%5][loc_2[1]])
    elif loc_1[0] == loc_2[0]:	# same column
        plaintext += (maze[loc_1[0]][(loc_1[1]-1+5)%5] + maze[loc_2[0]][(loc_2[1]-1+5)%5])
    else:
        plaintext += (maze[loc_1[0]][loc_2[1]] + maze[loc_2[0]][loc_1[1]])
    i += 1

# couple with double alphabet and the end X
length = len(plaintext)
if length % 2 == 0 and plaintext[length-1] == "X":
	plaintext = plaintext[:-1]
length = len(plaintext)
for i in range(0, length-3):
	if plaintext[i] == plaintext[i+2] and plaintext[i+1] == "X":
		plaintext = plaintext[:i+1] + plaintext[i+2:]

print("pliantext: ", plaintext)
