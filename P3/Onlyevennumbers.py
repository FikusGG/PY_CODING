chek=1
for i in range(10):
    n=int(input())
    if n%2!=0:chek-=1
if chek==1:print("YES")
else:print("NO")