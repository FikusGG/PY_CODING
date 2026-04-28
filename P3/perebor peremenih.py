# n,k,m=0,0,0
# # 28n+30k+31m=365.
# for n in range(1,30):
#     for k in range(1,30):
#         for m in range(1,30):
#             if 28*n + 30*k + 31*m ==365:
#                 print(n,k,m)

#   Старинная задача 🐮🌶️

# b,c,t=0,0,0
# # 20b+10c+t=200
# for b in range(1,101):
#     for c in range(1,101):
#         for t in range(1,101):
#             if (20*b+10*c+t==200)and(b+c+t==100):
#                 print(b,c,t)

# Гипотеза Эйлера о сумме степеней 🌶️🌶️

a,b,c,d,e=0,0,0,0,0
for a in range(1,151):
    for b in range(a,151):
        for c in range(b,151):
            for d in range(c,151):
                for e in range(d,151):
                    if (a**5)+(b**5)+(c**5)+(d**5)==(e**5):
                        print(a+b+c+d+e)