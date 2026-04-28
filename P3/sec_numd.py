n,sec=int(input()),0
while n!=0:
    if len(str(n))==2:sec=n%10
    n=n//10
print(sec)
