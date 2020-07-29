#!/usr/bin/env python3

v = [7, 12, 10, 8, 5, 19, 3, 90, 12]

i = 0
j = 1

while j < len(v):
    if v[j] > v[i]:
        j += 1        
    else:
        i += 1
        tmp = v[i]
        v[i] = v[j]
        v[j] = tmp        

tmp = v[0]
v[0] = v[i]
v[i] = tmp
print(v)