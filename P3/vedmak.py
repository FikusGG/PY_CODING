price=int(input())
counter=0
while price!=0:
    if price-25>=0:
        counter+=1
        price-=25
    elif price-10>=0:
        counter+=1
        price-=10
    elif price-5>=0:
        counter+=1
        price-=5
    elif price-1>=0:
        counter+=1
        price-=1
print(counter)