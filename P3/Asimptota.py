from math import log
n=int(input())
sum=0
for i in range(0,n):sum+=(1/(i+1))
print(sum-log(n))