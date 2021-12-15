# Cryptograhpy  
1. Substition Cipher  
	- Caesar Cipher  
	- Vigenere Cipher
	- Playfair Cipher
	- Lorenz Cipher
2. Transposition
	- Scytale Cipher
	- Rail Fence Cipher
3. Asymmetric Cipher
	- Merkle-Hellman Knapsack Cryptosystem
	- Kid-RSA & RSA
	- Diffie-Hellman Key Exachange Cryptosystem
4. Stream Cipher
	- RC4 Cipher
	- One-time Pad (OTP): key can only be used once (but its key management is too complicated)
5. GPG  
	e.g. stimulate the content of a mail
## Caesar Cipher
usage:  
`python3 Caesar_cipher.py key`

```
$ python3 python3 Caesar_cipher.py CAT
table:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
        CATBDEFGHIJKLMNOPQRSUVWXYZ
$encrypt or decrypt? (e/d) e
plaintext: HELLOWORLD
ciphertext:  GDKKNWNQKB
```

## Vigenere Cipher
usage:  
`python3 Vigenere_cipher.py key`

```
$ python3 Vigenere_cipher.py key
encrypt or decrypt?(e/d)
$ e
plaintext:
$ HELLOWORLD
ciphertext:  OIWWVAZCSH
```

## Playfair Cipher
`hw03-encrypyt.py` for encrypt; on the other hand, `hw03-decrypyt.py` for decrypt.  
usage:  
`python3 Playfair-encrypyt.py key`  
`python3 Playfair-decrypyt.py key`  

```
$ (echo cat; echo cat) | python3 Playfair-encrypt.py Apple
ICQGEQ
$ echo ICQGEQ | python3 Playfair-decrypt.py Apple
CATCAT
$ echo a fox jump over the lazy dog | python3 Playfair-encrypt.py 'playfair example'
YPQERTIFVAXEZBRAFVAGQD
```

## Lorenz Cipher
In Lorenz Cipher, encrypt is same as decrypt because of the XOR operation.  
usage:  
`python3 Lorenz.py chi mu psi`  
```
$ echo FREIGHTER | python3 Lorenz.py 12 7 9
+PGBUQZHR
$ echo +PGBUQZHR | python3 Lorenz.py 12 7 9
FREIGHTER
```

## Scytale Cipher
usage:  
`python3 Scytale-encrypt.py key`  
`python3 Scytale-decrypt.py key`  
```
$ (echo cat; echo cat) | python3 Scytale-encrypt.py 4
CTAGACTX
$ echo CTAGACTX | python3 Scytale-decrypt.py 4
CATCATGX
$ echo an apple a day keeps the doctor away | python3 Scytale-encrypt.py 7
ALYSOAYNEKTCWNAAEHTARPDEEOYXPAPDROI
```

## Rail Fence Cipher
usage:  
`python3 Rail_Fence-encrypt.py key`  
`python3 Rail_Fence-encrypt.py key -c`  
`python3 Rail_Fence-encrypt.py key --comma`  
The usage of decrypt is same as encrypt.  
If `-c`/`--comma` is exist, then the program will replace space with comma, and vice versa.  
```
$ (echo cat; echo cat) | python3 Rail_Fence-encrypt.py 4
CTAATC 
$ echo 'CTAATC ' | python3 Rail_Fence-decrypt.py 4
CAT CAT
$ echo an apple a day keeps the doctor away | python3 Rail_Fence-encrypt.py 7 -c
AA,NDYEDY,,,HOAAAKTCWP,E,TAPEESO,LPR
$ echo AA,NDYEDY,,,HOAAAKTCWP,E,TAPEESO,LPR | python3 Rail_Fence-decrypt.py 7
AN,APPLE,A,DAY,KEEPS,THE,DOCTOR,AWAY
```

## Merkle-Hellman Knapsack Cryptosystem
1. Generate key
```
[K]ey generation / [E]ncryption / [D]ecryption? k
Select the block size.
n? 8
Input a list of n superincreasing integers, separated by commas or spaces.
If you simply press , we shall randomly generate one for you.
W? 27 32 61 121 243 486 971 1943
Please input an integer larger than 3884
q? 3890
Please input an integer which is relatively prime with q.
r? 400
Please input an integer which is relatively prime with q.
r? 2001
=========================
Announce your public key:
n = 8
B = [3457, 1792, 1471, 941, 3883, 3876, 1861, 1833]
q = 3890
=========================
```
2. Encryption
```
[G]enerate key | [E]ncryption | [D]ecryption? E
n? 8
Input a list of n integers, separated by commas or spaces.
B? 295, 592, 301, 14, 28, 353, 120, 236
q? 881
Plaintext - Encrypt me!!!
Ciphertext: [1181, 1394, 1249, 1027, 1171, 907, 1260, 301, 1510, 1482, 537, 537, 537]
```
3. Decryption
```
[G]enerate key | [E]ncryption | [D]ecryption? D
Select the block size.
n? 8
Input a list of n superincreasing integers, separated by commas or spaces.
If you simply press , we shall randomly generate one for you.
W? 2 7 11 21 42 89 180 354
Please input an integer larger than 706
q? 881
Please input an integer which is relatively prime with q.
r? 588
Input ciphertext (separated by spaces) - 1181, 1394, 1249, 1027, 1171, 907, 1260, 301, 1510, 1482, 537, 537, 537
Plaintext: 69 110 99 114 121 112 116 32 109 101 33 33 33
Encrypt me!!!
```

## RSA
- Encryption
```
[E]ncryption, [D]ecryption, or [Q]uit -- E
2       3       5       7       11
13      17      19      23      29
31      37      41      43      47
53      59      61      67      71
73      79      83      89      97
Select two prime numbers from the above, separated by a space.
Or press ENTER and I'll randomly select two for you -- 5 29
The two prime numbers are 5 and 29.
n = 5 * 29 = 145
Possible values of e which are coprime to 28:
3       5       9       11      13      15      17      19      23      25     27
Choose one -- 11
You may publish your public key (n,e) = (145,11)
and keep your private key (n,d) = (145,23) secret.
Plaintext - ABC
110 61 138
```
- Decryption
```
[E]ncryption, [D]ecryption, or [Q]uit -- D
Your private key (n, d), separated by a space or comma -- 145 23
Ciphertext (integers separated by spaces) -- 110 61 138
65 66 67
Plaintext - ABC
```

### Kid-RSA
- Encryption
```
[E]ncryption, [D]ecryption, or [Q]uit -- e
Input 4 integers a, b, a', b' -- 9 11 5 8
You may publish your public key (n,e) = (4048,499)
and keep your private key (n,d) = (4048,795) secret.
Plaintext - ABC
51 550 1049
```
- Decryption
```
[E]ncryption, [D]ecryption, or [Q]uit -- d
Your private key (n, d), separated by a space or comma -- 4048,795
Ciphertext (integers separated by spaces) -- 51 550 1049
65 66 67
Plaintext - ABC
```

## Diffie-Hellman key exchange
the user inputs the values of g, p, let's enumerate all possible values of a and b (from 1 to p-1). 
Show the value of g^ab mod p. Investigate whether there are good values of a, b or not.
```
g, p = 5, 23
  | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22
--+------------------------------------------------------------------
 1| 5  2 10  4 20  8 17 16 11  9 22 18 21 13 19  3 15  6  7 12 14  1
 2| 2  4  8 16  9 18 13  3  6 12  1  2  4  8 16  9 18 13  3  6 12  1 Bad
 3|10  8 11 18 19  6 14  2 20 16 22 13 15 12  5  4 17  9 21  3  7  1
 4| 4 16 18  3 12  2  8  9 13  6  1  4 16 18  3 12  2  8  9 13  6  1 Bad
 5|20  9 19 12 10 16 21  6  5  8 22  3 14  4 11 13  7  2 17 18 15  1
 6| 8 18  6  2 16 13 12  4  9  3  1  8 18  6  2 16 13 12  4  9  3  1 Bad
 7|17 13 14  8 21 12 20 18  7  4 22  6 10  9 15  2 11  3  5 16 19  1
 8|16  3  2  9  6  4 18 12  8 13  1 16  3  2  9  6  4 18 12  8 13  1 Bad
 9|11  6 20 13  5  9  7  8 19  2 22 12 17  3 10 18 14 16 15  4 21  1
10| 9 12 16  6  8  3  4 13  2 18  1  9 12 16  6  8  3  4 13  2 18  1 Bad
11|22  1 22  1 22  1 22  1 22  1 22  1 22  1 22  1 22  1 22  1 22  1 Bad
12|18  2 13  4  3  8  6 16 12  9  1 18  2 13  4  3  8  6 16 12  9  1 Bad
13|21  4 15 16 14 18 10  3 17 12 22  2 19  8  7  9  5 13 20  6 11  1
14|13  8 12 18  4  6  9  2  3 16  1 13  8 12 18  4  6  9  2  3 16  1 Bad
15|19 16  5  3 11  2 15  9 10  6 22  4  7 18 20 12 21  8 14 13 17  1
16| 3  9  4 12 13 16  2  6 18  8  1  3  9  4 12 13 16  2  6 18  8  1 Bad
17|15 18 17  2  7 13 11  4 14  3 22  8  5  6 21 16 10 12 19  9 20  1
18| 6 13  9  8  2 12  3 18 16  4  1  6 13  9  8  2 12  3 18 16  4  1 Bad
19| 7  3 21  9 17  4  5 12 15 13 22 16 20  2 14  6 19 18 11  8 10  1
20|12  6  3 13 18  9 16  8  4  2  1 12  6  3 13 18  9 16  8  4  2  1 Bad
21|14 12  7  6 15  3 19 13 21 18 22  9 11 16 17  8 20  4 10  2  5  1
22| 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1 Bad
```