# Тз

# кол-во цифр 3

# кол-во последней цифры

# сумму его цифр, больших пяти

# произведение цифр, больших семи 
# (если цифр больших семи нет, то вывести 1, 
# если такая цифра одна, то вывести её)

# сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).

n=int(input())
count_three=0
count_lustnumb=0
count_chet=0
sum_bet_five=0
proizv_bet_seven=1
counter_z_f=0
const_lust=n%10
while n!=0:
    lust_numb=n%10
    if lust_numb==3:count_three+=1
    elif lust_numb==const_lust:count_lustnumb+=1
    elif lust_numb&2==0:count_chet+=1
    elif lust_numb>5:sum_bet_five+=lust_numb
    elif lust_numb>7:proizv_bet_seven*=lust_numb
    elif lust_numb in [0,5]:counter_z_f+=1
    n=n//10
print(count_three,count_lustnumb,count_chet,sum_bet_five,proizv_bet_seven,counter_z_f,sep='\n')
    








