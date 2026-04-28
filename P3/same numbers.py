# n=int(input())
# same=True
# while len(str(n))!=1:
#     last1=n%10
#     n=n//10
#     last2=n%10
#     if last1!=last2:same=False
# if same==True:print("YES")
# else:print("NO")
n=int(input())
same=True
while len(str(n))!=1:
    last1=n%10
    n=n//10
    last2=n%10
    if last1>last2:same=False
if same==True:print("YES")
else:print("NO")