#!/bin/env python3
import math
import random

option = input("[E]ncryption, [D]ecryption, or [Q]uit -- ")
def random_choose():
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    cnt1 = random.randint(0, len(prime_list)-1)
    cnt2 = random.randint(0, len(prime_list)-1)
    while cnt2 == cnt1:
        cnt2 = random.randint(0, len(prime_list)-1)
    return prime_list[cnt1], prime_list[cnt2]

def euclid(n):
    result = []
    for i in range(n):
        if math.gcd(i, n) == 1:
            result.append(str(i))
    return result

def encryption():
    print("2       3       5       7       11")
    print("13      17      19      23      29")
    print("31      37      41      43      47")
    print("53      59      61      67      71")
    print("73      79      83      89      97")
    print("Select two prime numbers from the above, separated by a space.")
    prime_num = input("Or press ENTER and I'll randomly select two for you -- ")
    if prime_num == '':
        p, q = randan_choose()
    else:
        p, q = list(map(int, prime_num.split(" ")))
    print("The two prime numbers are", p, "and", q, ".")
    n = p * q
    print("n = ", p, "*", q, "=", n)
    eu_n = euclid(n)
    num_eu = len(eu_n)
    print("Possible values of e which are coprime to", num_eu, ": ")
    print(" ".join(eu_n))
    e = int(input("Choose one -- "))
    print("You may publish your public key (n,e) = (", n, ",", e, ")")
    d = pow(e, -1, num_eu)
    print("and keep your private key (n,d) = (", n, ",", d, ") secret.")
    plaintext = input("Plaintext - ")
    cipher = []
    for i in range(len(plaintext)):
        cipher.append(str(pow(ord(plaintext[i]), e) % n))
    print(" ".join(cipher))

def decryption():
    private = input("Your private key (n, d), separated by a space or comma -- ").replace(",", " ")
    n, d = list(map(int, private.split(" ")))
    ciphertext = input("Ciphertext (integers separated by spaces) -- ")
    cipher = list(map(int, ciphertext.split(" ")))
    plain = []
    for i in range(len(cipher)):
        plain.append(str(pow(cipher[i], d) % n))
    plaintext = ""
    print(" ".join(plain))
    for i in range(len(plain)):
        plaintext += chr(int(plain[i]))
    print(plaintext)

def main():
    if option.upper() == "E":
        encryption()
    elif option.upper() == "D":
        decryption()
    else:
        return

if __name__ == "__main__":
    main()
