from math import *
a,b,c=float(input()),float(input()),float(input())
d=(b**2)-4*a*c
if d<0:print("Нет корней")
elif d==0:print(-(b/(2*a)))
else:
    print((-b-sqrt(d)/(2*a)))
    print((-b+sqrt(d)/(2*a)))