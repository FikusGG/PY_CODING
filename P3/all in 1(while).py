# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
suma=0
kol=0
proizv=1
first_num=0
n=int(input())
theLust=n%10
while n!=0:
    last_num=n%10
    suma+=last_num
    kol+=1
    proizv*=last_num
    if len(str(n))==1:
        first_num=n
    n=n//10
lustANDfirst=theLust+first_num
sredArefm=suma/kol
print(suma,kol,proizv,sredArefm,first_num,lustANDfirst,sep="\n")