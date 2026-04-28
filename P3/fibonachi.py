a,b,c=1,0,0
n=int(input())
for _ in range(n):
    c=a+b
    a=b
    b=c
    print(c,sep=" ", end=" ")
