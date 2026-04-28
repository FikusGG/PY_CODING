n=int(input())
sum=0
for i in range(n):
    if ((i+1)**2)%10 in [2,5,8]:
        sum+=i+1
print(sum)
