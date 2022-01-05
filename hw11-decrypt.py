#!/bin/env python3
import sys

len_argv = len(sys.argv)
str_key = ""
for i in range(1, len_argv):
    str_key += sys.argv[i]

def two_ascii(text):
    result = []
    for i in range(len(text)):
        result.append(ord(text[i]))
    return result

def shuffle_S(S, key):
    j = 0
    for i in range(len(S)):
        j = (j + S[i] + key[i%len(key)]) % len(S)
        S[i], S[j] = S[j], S[i]
    return S

def generate_key_stream(S, text):
    j = 0
    i = 0
    key_stream = []
    for k in range(len(text)):
        i = (i + 1) % len(S)
        j = (j + S[i]) % len(S)
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % len(S)
        key_stream.append(S[t])
    return key_stream

def two_decimal(text):
    result = []
    for i in range(0, len(text), 2):
        result.append(int(text[i:i+2], 16))
    return result

def main():
    key = two_ascii(str_key)
    S = list(range(0, 256))
    S = shuffle_S(S, key)
    ciphertext = input()
    cipher = two_decimal(ciphertext)
    Key_stream = generate_key_stream(S, cipher)
    plaintext = ""
    for i in range(len(cipher)):
        plaintext += chr(cipher[i] ^ Key_stream[i])
    print(plaintext)

if __name__ == "__main__":
    main()
