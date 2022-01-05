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
def main():
    key = two_ascii(str_key)
    S = list(range(0, 256))
    S = shuffle_S(S, key)
    plaintext = input()
    plain = two_ascii(plaintext)
    Key_stream = generate_key_stream(S, plain)
    ciphertext = ""
    for i in range(len(plain)):
        ciphertext += hex(plain[i] ^ Key_stream[i])[2:].upper()
    print(ciphertext)

if __name__ == '__main__':
    main()
