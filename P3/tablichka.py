# n=int(input())
# for j in range(n):
#     for _ in range(3):
#         print(n,end=' ')
#     print()
# n=int(input())

# for j in range(n):
#     for _ in range(5):
#         print(j+1,end=' ')
#     print()

# n=int(input())
# for j in range(1,n+1):
#     for i in range(9):
#         print(f"{j} + {i+1} =",j+(i+1))
#     print()

# Звёздный треугольник 🌟🌶️🌶️

# n=int(input())
# for i in range((n//2+1)):
#     for _ in range(i+1):
#         print("*",end="")
#     print()
# for j in range(n//2,0,-1):
#     for _ in range(j):
#         print("*",end="")
#     print()

# Численный треугольник 1

# n=int(input())
# for i in range(1,n+1):
#     for _ in range(i):
#         print(i,end="")
#     print()

# # Численный треугольник 2
# count=1
# n=int(input())
# for i in range(1,n+1):
#     for _ in range(i):
#         print(count,end=" ")
#         count+=1
#     print()

# # # Численный треугольник 3 🌶️
# count=1
# n=int(input())
# for i in range(1,(n*2)+1,2):
#     count=1
#     for _ in range(i//2+1):
#         print(count,end="")
#         count+=1
#     count-=2
#     for _ in range(i//2):
#         print(count,end="")
#         count-=1
#     print()
    
# # Делители-1 🌶️
# summ=0
# maxsumm=0
# maxNumb=0
# a,b=int(input()),int(input())
# for i in range(a,b+1):
#     summ=0
#     for j in range(1,i+1):
#         if i%j==0:
#             summ+=j
#     if summ>=maxsumm:
#         maxsumm=summ
#         maxNumb=i
# print(maxNumb,maxsumm,sep=" ")

# # Делители-2
# deliteli=0
# n=int(input())
# for i in range(1,n+1):
#     deliteli=0
#     for j in range(1,i+1):
#         if i%j==0:
#             deliteli+=1
#     print(i,"+"*deliteli,sep="")

# Цифровой корень 🌶️
# n=int(input())
# while n>9:
#     sum=0
#     while n>0:
#         last_num=n%10
#         sum+=last_num
#         n=n//10
#     n=sum
# print(n)

# # Сумма факториалов ❗
# n=int(input())
# sum=0
# for i in range(1, n+1):
#     fac=1
#     for j in range(1,i+1):
#         fac*=j
#     sum+=fac
# print(sum)

# Простые числа 👌
a,b=int(input()),int(input())
for i in range(a,b+1):
    deliteli=0
    for j in range(1,i+1):
        if i%j==0:
            deliteli+=1
    if deliteli==2:
        print(i)

