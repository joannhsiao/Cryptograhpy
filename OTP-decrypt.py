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

def digit2char(digit):
    i = 0
    alphabet = ""
    while i < len(digit):
        tmp = ""
        if int(digit[i]) in list(table.values()):
            tmp = digit[i]
        else:
            tmp += digit[i] + digit[i+1]
            i += 1
        if i <= len(digit)-3 and tmp == digit[i+1] and digit[i+1] == digit[i+2]:
            char = tmp
            i += 2
        else: 
            char = list(table.keys())[list(table.values()).index(int(tmp))]
        if char == "FIG":
            char = ""
        alphabet += char
        i += 1
    return alphabet

def char2digit(alphabet):
    if alphabet in table:
        return str(table[alphabet])
    else:
        tmp = ""
        for i in range(3):
            tmp += str(alphabet)
        return tmp

def cal(text, key):
    plain = ""
    for i in range(len(text)):
        plain += str((int(text[i]) - int(key[i])) % 10)
    return plain

def main():
    ciphertext = input()
    with open(key_file, "r") as f:
        key = f.read(len(ciphertext)).upper()
    key_string = ""
    for i in range(len(key)):
        key_string += char2digit(key[i])
    if len(ciphertext) < len(key_string):
        key_string = key_string[0:len(ciphertext)]
    plain = cal(ciphertext, key_string)
    print(digit2char(plain))

if __name__ == "__main__":
    main()
