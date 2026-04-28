#  Заглавные буквы 🔠
# s=input()
# if s.title()==s:print("YES")
# else:print("NO")
# s.swapcase

# s=input()
# if ("хорош") in s.lower():print("YES")
# elif ("хороший") in s.lower():print("YES")
# else:print("NO")

azb="abcdefghijklmnopqrstuvwxyz"
s=input()
count=0
for i in azb:
    for f in s:
        if i==f:
            count+=1
print(count)