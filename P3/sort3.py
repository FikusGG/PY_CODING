a,b,c=int(input()),int(input()),int(input())
f=(a+b+c)-(min(a,b,c)+max(a,b,c))
print(max(a,b,c),f,min(a,b,c),sep='\n')