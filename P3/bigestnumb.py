m=int(input())
big=0
bigest=0
def f(n):
    if n>bigest:
        big=bigest
        bigest=n
while m>=0:
    m-=1
    n=int(input())
    f(n)
print(bigest,big,sep=('\n'))