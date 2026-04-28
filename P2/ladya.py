x1,y1,x2,y2=int(input()),int(input()),int(input()),int(input())
if (x1==x2 and((0<(y2-y1)<=8)or(0<(y1-y2)<=8)))or(y1==y2 and((0<(x2-x1)<=8)or(0<(x1-x2)<=8))):print("YES")
else:print("NO")