#!/bin/env python3
# lorenz cipher encrypt/decrypt
# mu: . -> 0, x -> 1
import sys
chi_key = int(sys.argv[1])
mu_key = int(sys.argv[2])
psi_key = int(sys.argv[3])

Baudot_Code = {"A": 0b11000, "B": 0b10011, "C": 0b01110, "D": 0b10010, "E": 0b10000, "F": 0b10110, "G": 0b01011, 
"H": 0b00101, "I": 0b01100, "J": 0b11010, "K": 0b11110, "L": 0b01001, "M": 0b00111, "N": 0b00110, "O": 0b00011, 
"P": 0b01101, "Q": 0b11101, "R": 0b01010, "S": 0b10100, "T": 0b00001, "U": 0b11100, "V": 0b01111, "W": 0b11001, 
"X": 0b10111, "Y": 0b10101, "Z": 0b10001, "4": 0b01000, "3": 0b00010, "9": 0b00100, "8": 0b11111, "+": 0b11011, 
"/": 0b00000}
chi = "N4LNFUWKHGR9ZD4/VMQ4BYH"
mu = "0010111110001"
psi = "PNTKTUGFLFLX4NAOIB4"

plaintext = ""
while True:
    try:
        n = input().replace("\n", "")
        plaintext += n
    except EOFError:
        break

plaintext = plaintext.upper().replace(" ", "")
length = len(plaintext)

def psi_enable(i):
    if mu[i - 1] == "1":
        return True
    else:
        return False

def rotate(i, j, k):
    if i == len(chi):
        i = 1
    else:
        i += 1
    if psi_enable(j):
        if k == len(psi):
            k = 1
        else:
            k += 1
    if j == len(mu):
        j = 1
    else:
        j += 1
    return (i, j, k)

ciphertext = ""
for i in range(0, length):
    cipher = Baudot_Code[plaintext[i]] ^ Baudot_Code[chi[chi_key - 1]] ^ Baudot_Code[psi[psi_key - 1]]
    ciphertext += list(Baudot_Code.keys())[list(Baudot_Code.values()).index(cipher)]
    chi_key, mu_key, psi_key = rotate(chi_key, mu_key, psi_key)

print(ciphertext)
