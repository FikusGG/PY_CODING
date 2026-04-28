n=int(input())
rn=''
while n!=0:
    last_num=n%10
    rn=str(rn)+str(last_num)
    n=n//10
print(rn)
