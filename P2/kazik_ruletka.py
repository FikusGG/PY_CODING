# 1-10 ч к
# 11-18 к ч
# 19 28 ч к 
# 29 36 к ч
numb=int(input())
if numb==0:print("зеленый")
elif numb>36 or numb<0:print("ошибка ввода")
elif numb==1 or numb==2 or numb==3 or numb==3 or numb==4 or numb==5 or numb==6 or numb==7 or numb==8 or numb==9 or numb==10 or numb==19 or numb==20 or numb==21 or numb==22 or numb==23 or numb==24 or numb==25 or numb==26 or numb==27 or numb==28:
    if numb%2==0:print("черный")
    else:print("красный")
else:
    if numb==1 or numb%2==0:print("красный")
    else:print("черный")
