n=int(input())
l=[]
while n!=0:
    last_num=n%10
    l.append(last_num)
    n=n//10
print(f'Максимальная цифра равна {max(l)}',f'Минимальная цифра равна {min(l)}',sep="\n")