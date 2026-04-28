# count = 0
# p = 0
# for i in range(1, 10):
#     x = int(input())
#     if x > 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(x)
#     print(p)
# else:
#     print('NO')

count,p=0,1
for _ in range(10):
    x = int(input())
    if x >= 0:
        p=p*x
        count+=1
if count > 0:print(count,p,sep="\n")
else:print('NO')
#20 из 20