a,b,c=map(int,input().split())
s=0
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))**0.5
print('%0.2f'%a)