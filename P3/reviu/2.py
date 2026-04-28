# mx = 0
# s = 0
# for i in range(11):(3)
#     x = int(input())
#     if x < 0:
#         s = x (1)
#     (2)if x > mx:
#         mx = x
# print(s)
# print(mx)
max_min=(-10)**101
summ=0
count=0
for _ in range(10):
    x = int(input())
    if x < 0:
        summ+=x
        count+=1
        if x>max_min:
            max_min=x
if count==0: print("NO")
else:
    print(summ)
    print(max_min)
#20 из 20