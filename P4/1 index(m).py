# В столбик 1
# n=str(input())
# for i in range(0,len(n),2):
#     print(n[i])

# В столбик 2
# s=input()
# for i in range(len(s)-1,-1,-1):
#     print(s[i])

# ФИО
# i,f,o=input(),input(),input()
# print(f[0]+i[0]+o[0])

# Цифра 1
# s=input()
# sum=0
# for i in range(0,len(s)):
#     sum+=int(s[i])
# print(sum)

# цифра 2
# s=input()
# chek=True
# for i in range(10):
#     if str(i) in s: chek=False
# if chek==False:print('Цифра')
# else:print('Цифр нет')

# Сколько раз?
# m,n=0,0
# # m"*" n"+"
# s=input()
# for i in range(len(s)):
#     if s[i]=="+":n+=1
#     if s[i]=="*":m+=1
# print(f"Символ + встречается {n} раз")
# print(f"Символ * встречается {m} раз")

# Одинаковые соседи
# s=input()
# cont=0
# for i in range(1,len(s)):
#     if s[i-1]==s[i]:
#         cont+=1
# print(cont)

# Гласные и согласные 🔠
# glas='ауоыиэяюеАУОЫИЭЯЮЕ'
# sogl='бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
# c_glas=0
# c_sogl=0
# s=input()
# for i in range(len(s)):
#     if s[i] in glas:c_glas+=1
#     if s[i] in sogl:c_sogl+=1
# print(f'Количество гласных букв равно {c_glas}')
# print(f'Количество согласных букв равно {c_sogl}')

# Decimal to Binary 🔟
n=int(input())
binary=""
while n!=0:
    # if n%2==0:
    #     binary+='0'
    # else:
    #     binary+='1'
    binary+=str(n%2)
    n//=2
print(binary)
