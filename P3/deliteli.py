n,summ=int(input()),0
for i in range(n):
    if (n%(i+1))==0:summ+=(i+1)
print(summ)