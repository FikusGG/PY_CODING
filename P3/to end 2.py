word=input()
counter=0
while word not in ["хватит","достаточно","стоп"]:
    counter+=1
    word=input()
print(counter)