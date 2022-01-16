#!/bin/env python3
import sys

key_file = sys.argv[1]
table = {"CODE":0, "B":70, "P":80, "FIG":90,
         "A":1, "C":71, "Q":81, ".":91,
         "E":2, "D":72, "R":82, ":":92,
         "I":3, "F":73, "S":83, "'":93,
         "N":4, "G":74, "U":84, " ":94,
         "O":5, "H":75, "V":85, "+":95,
         "T":6, "J":76, "W":86, "-":96,
         "K":77, "X":87, "=":97,
         "L":78, "Y":88, "REQ":98,
         "M":79, "Z":89, "SPC":99}

def char2digit(alphabet):
    if alphabet in table:
        return str(table[alphabet])
    else:
        tmp = ""
        for i in range(3):
            tmp += str(alphabet)
        return tmp

def cal(text, key):
    cipher = ""
    for i in range(len(text)):
        cipher += str((int(text[i]) + int(key[i])) % 10)
    print(cipher)

def main():
    plaintext = input().upper()
    plain_stream = []
    plain = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >= 48 and ord(plaintext[i]) <= 57:
            if ord(plaintext[i-1]) < 48 or ord(plaintext[i-1]) > 57:
                plain_stream.append("FIG")
        plain_stream.append(plaintext[i])
        if ord(plaintext[i]) >= 48 and ord(plaintext[i]) <= 57:
            if i!= len(plaintext) - 1 and (ord(plaintext[i+1]) < 48 or ord(plaintext[i+1]) > 57):
                plain_stream.append("FIG")
    for i in range(len(plain_stream)):
        plain += char2digit(plain_stream[i])
    with open(key_file) as f:
        key = f.read(len(plain)).upper()
    key_string = ""
    for i in range(len(key)):
        key_string += char2digit(key[i])
    if len(plain) < len(key_string):
        key_string = key_string[0:len(plain)]
    cal(plain, key_string)

if __name__ == "__main__":
    main()
