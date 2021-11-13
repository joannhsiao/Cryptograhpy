import sys

key = sys.argv[1]
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
transfer = ''.join(sorted(set(key), key=key.index))

i = 0
while i != len(table):
    if table[i] not in transfer:
        transfer += str(table[i])
    i += 1

print("table: ", table)
print("       ", transfer)

motion = input("encrypt or decrypt? (e/d)")

if motion == "e":
	n = input("plaintext: ")
	ans = ""
	for j in range(len(n)):
		ans += str(transfer[table.find(n[j])])
	print("ciphertext: ", ans)
else: 
	n = input("ciphertext: ")
	ans = ""
	for j in range(len(n)):
		ans += str(table[transfer.find(n[j])])
	print("plaintext: ", ans)