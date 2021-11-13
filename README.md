# Cryptograhpy
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
<p>`hw03-encrypyt.py` for encrypt; on the other hand, `hw03-decrypyt.py` for decrypt</p>
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