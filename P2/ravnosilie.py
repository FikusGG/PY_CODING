chislo=int(input())
a1=chislo//1000
a2=(chislo//100)%10
a3=(chislo//10)%10
a4=chislo%10
if a1+a4==a2-a3: print('ДА')
else: print('НЕТ')