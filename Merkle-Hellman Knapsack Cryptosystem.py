#!/bin/env python3
import math
import sys
import random

option = input("[K]ey generation| [E]ncryption | [D]ecryption?")
print("Select the block size.")
n = int(input("n?"))

def random_num(n):
    cnt = 1
    a = [0] * n
    while cnt < n:
        num = random.randint(0, sys.maxsize)
        while num < sum(a):
            num = random.randint(0, sys.maxsize)
        a[cnt-1] = num
        cnt += 1
    return a

def generate_key(n):
    print("Input a list of n superincreasing integers, separated by commas or spaces.")
    print("If you simply press , we shall randomly generate one for you.")
    W = input("W? ").replace(",", "")
    if W == "\n":
        A = random_num(n)
    else:
        A = list(map(int, W.split(" ")))
    print("Please input an integer larger than ", sum(A))
    q = int(input("q? "))
    while q < sum(A):
        print("Please input an integer larger than ", sum(A))
        q = int(input("q? "))
    print("Please input an integer which is relatively prime with q.")
    r = int(input("r? "))
    while math.gcd(q, r) != 1:
        print("Please input an integer which is relatively prime with q.")
        r = int(input("r? "))
    B = [(a * r) % q for a in A]

    print("=========================")
    print("Announce your public key:")
    print("n = ", n)
    print("B = ", B)
    print("q = ", q)
    print("=========================")

def encryption(n):
    print("Input a list of n integers, separated by commas or spaces.")
    b = input("B? ").replace(",", "")
    B = list(map(int, b.split(" ")))
    plaintext = input("Plaintext - ")
    ciphertext = []
    for i in range(len(plaintext)):
        Ascii = str(bin(ord(plaintext[i])))[2:].zfill(n)
        num = 0
        for j in range (n):
            num += int(Ascii[j]) * B[j]
        ciphertext.append(num)
    print("Ciphertext: ", ciphertext)

def decryption(n):
    print("Input a list of n superincreasing integers, separated by commas or spaces.")
    print("If you simply press , we shall randomly generate one for you.")
    W = input("W? ")
    if W == "\n":
        A = random_num(n)
    else:
        A = list(map(int, W.split(" ")))
    print("Please input an integer larger than ", sum(A))
    q = int(input("q? "))
    while q < sum(A):
        print("Please input an integer larger than ", sum(A))
        q = int(input("q? "))
    print("Please input an integer which is relatively prime with q.")
    r = int(input("r? "))
    while math.gcd(q, r) != 1:
        print("Please input an integer which is relatively prime with q.")
        r = int(input("r? "))
    ciphertext = input("Input ciphertext (separated by spaces) - ").replace(",", "")
    cipher = list(map(int, ciphertext.split(" ")))
    x = pow(r, -1, q)
    plaintext = []
    for i in range(len(cipher)):
        y = (cipher[i] * x) % q
        tmp = [0] * n
        for j in range(n-1, -1, -1):
            if y >= A[j]:
                tmp[j] = 1
                y -= A[j]
        plain = ""
        for j in range(n):
            plain += str(tmp[j])
        plaintext.append(int(plain, 2))
    print("Plaintext: ", plaintext)
    Plaintext = []
    for i in range(len(plaintext)):
        Plaintext.append(chr(plaintext[i]))
    print("".join(Plaintext))

if option.upper() == "K":
    generate_key(n)
elif option.upper() == "E":
    encryption(n)
elif option.upper() == "D":
    decryption(n)
else:
    print("Follow the rule please!!")
