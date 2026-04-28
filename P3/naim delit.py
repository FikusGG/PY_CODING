n=int(input())
for i in range(1,n):
    if n%(i+1)==0:
        delitel=i+1
        break
print(delitel)