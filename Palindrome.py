n=int(input())
s=0
temp=n
while temp:
    r=temp%10
    s=s*10+r
    temp//=10
if s==n:
        print("True")
else:
        print("False")