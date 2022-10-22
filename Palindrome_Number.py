t=int(input())
for i in range(1,t+1):
    a=int(input())
    temp=a
    rev=0
    for i in range(1,temp+1):
        while temp:
            rem=temp%10
            rev=rev*10+rem
            temp=temp//10
    if(rev==a):
                print('True')
    else:
                    print('False')