# Количество слов
# s=input()
# print(int(s.count(" "))+1)

# Минутка генетики 🧬
# s=input()
# aden=0
# guan=0
# chit=0
# timin=0
# s=s.lower()
# aden+=s.count("а")
# guan+=s.count("г")
# chit+=s.count("ц")
# timin+=s.count("т")
# print("Аденин:",aden)
# print("Гуанин::",guan)
# print("Цитозин:",chit)
# print("Тимин:",timin)

# Очень странные дела 📻
# n=int(input())
# con=0
# for _ in range(n):
#     s=input()
#     if s.count('11')>=3:con+=1
# print(con)

# Количество цифр
# s=input()
# son=0
# for i in range(10):
#     son+=int(s.count(str(i)))
# print(son)

# .com or .ru 🌐
# s=input()
# if s.endswith('.com') or s.endswith('.ru'):print("YES")
# else:print('NO')

# Самый частотный символ
# s=input()
# max_col=-1
# max_s=-1
# con=1
# for i in range(1,len(s)):
#     if s[i-1]==s[i]:
#         con+=1
#     else:
#         if max_col<con:
#             max_col=con
#             max_s=s[i-1]
#         else:
#             continue
#         con=1
# print(max_s)

# s=str(input())
# if "f" not in s :
#     print("NO")
# else:
#     index=s.find("f")
#     s = s[:index] + "a" + s[index+1:]
#     if "f" in s:
#         index2=s.rfind("f")
#         print(index,index2)
#     elif "f" not in s:
#         print(index)

s=str(input())
index1=s.find("h")
index2=s.rfind("h")
a=(s[:index1])
b=(s[index2+1:])
res=a+b
print(res)