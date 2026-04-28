numb=int(input())
a=numb//100
b=(numb%100)//10
c=numb%10
r=max(a,b,c)-min(a,b,c)
m=a+b+c-min(a,b,c)-max(a,b,c)
if m==r:print("Число интересное")
else:print("Число неинтересное")