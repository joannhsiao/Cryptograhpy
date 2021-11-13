#!/bin/env python3
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

plaintext = ""
while True:
    try:
        n = input().replace("\n", "")
        plaintext += n
        plaintext += " "
    except EOFError:
        break
plaintext = plaintext[0:-1].upper()
if args.comma:
    plaintext = plaintext.replace(" ", ",")
length = int(len(plaintext))

def fetch(text, key, num, length):
    result = ""
    for i in range(length):
        if i % num == key:
            result += text[i]
        if i % num == num - key and i % num != 0 and i % num != int(num/2):
            result += text[i]
    return result

key = int(args.key)
ciphertext = ""
cmd = (key - 1) * 2
for i in range(key):
    ciphertext += fetch(plaintext, i, cmd, length)
print(ciphertext)
