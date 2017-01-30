#!/usr/bin/env python

print("input Caesar cipher: ", end = "")
cipher = input()
print("input plain text (Not knowing word is *): ", end = "")
plain = input()

list_cip = list(cipher)
list_pla = list(plain)
num = 0
key_num = 0
num_word = ord('z') - ord('a') + 1
perf_pla = []

for i in list_pla:
    if i != '*':
        break
    else:
        num += 1

if ord(list_pla[num]) > ord(list_cip[num]):
    key_num = ord(list_cip[num]) + num_word - ord(list_pla[num])
else:
    key_num = ord(list_cip[num]) - ord(list_pla[num])

for i in list_cip:
    if(ord(i) >= ord('a')):
        if(ord(i) - key_num < ord('a')):
            perf_pla.append(chr(ord(i) + num_word - key_num))
        else:
            perf_pla.append(chr(ord(i) - key_num))
    else:
        if(ord(i) - key_num < ord('A')):
            perf_pla.append(chr(ord(i) + num_word - key_num))
        else:
            perf_pla.append(chr(ord(i) - key_num))

plain = "".join(perf_pla)
print(key_num)
print(plain)
