#!/bin/env python3
import math
import argparse

parser = argparse.ArgumentParser(description="Rail Fence Cipher")
parser.add_argument("key", help="Number of rows (rails)")
parser.add_argument("-c", "--comma", help="display spaces as commas ", action='store_true')
args = parser.parse_args()
print(__file__, args.key)
if args.comma:
    print("Show a space as ','")
else:
    print("Show a space as ' '")

ciphertext = input()

if args.comma:
    ciphertext = ciphertext.replace(",", " ")
length = int(len(ciphertext))
            
def fetch(text, key, length, pair):
    result = ""
    list = []
    cnt = (key - 1) * 2
    for i in range(key):
        addnum = i
        for j in range(pair + 1):
            if i == 0 or i == key - 1:
                if j != 0:
                    addnum += cnt
                if addnum < length:
                    list.append(addnum)
            else:
                if j != 0:
                    addnum += cnt - 2 * i
                if addnum < length:
                    list.append(addnum)
                if j != 0:
                    addnum += 2 * i
                    if addnum < length:
                        list.append(addnum)

    for i in range(length):
        result += text[list.index(i)]
    return result

key = int(args.key)

plaintext = ""
pair = math.ceil((length - 4) / (key - 1))
plaintext = fetch(ciphertext, key, length, pair)
print(plaintext)
