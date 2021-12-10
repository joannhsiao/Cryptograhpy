#!/bin/env python3
option = input("[E]ncryption, [D]ecryption, or [Q]uit -- ")
def key_generation(a, b, a1, b1):
    M = a *  b - 1
    e = a1 * M + a
    d = b1 * M + b
    n = (e * d - 1) / M
    return int(e), int(d), int(n)

def encryption(a, b, a1, b1): 
    e, d, n = key_generation(a, b, a1, b1)
    print("You may publish your public key (n,e) = (", n, ", ", e, ")")
    print("and keep your private key (n,d) = (",n, ", ", d, ") secret.")
    plaintext = input("Plaintext - ")
    cipher = []
    for i in range(len(plaintext)):
        cipher.append(str((ord(plaintext[i]) * e) % n))
    ciphertext = " ".join(cipher)
    print(ciphertext)

def decryption():
    private = input("Your private key (n, d), separated by a space or comma -- ").replace(",", " ")
    n, d = list(map(int, private.split(" ")))
    ciphertext = input("Ciphertext (integers separated by spaces) -- ")
    cipher = list(map(int, ciphertext.split(" ")))
    plain = []
    for i in range(len(cipher)):
        plain.append(str((cipher[i] * d) % n))
    print(" ".join(plain))
    plaintext = ""
    for i in range(len(plain)):
        plaintext += chr(int(plain[i]))
    print("Plaintext - ", plaintext)

def main():
    if option.upper() == "E":
        ints = input("Input 4 integers a, b, a', b' -- ")
        a, b, a1, b1 = list(map(int, ints.split(" ")))
        encryption(a, b, a1, b1)
    elif option.upper() == "D":
        decryption()
    else:
        return

if __name__ == "__main__":
    main()
