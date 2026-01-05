n=int(input("enter a number"))
temp=n
sum=0
while(temp>0):
    rem=temp%10
    power=pow(rem,3)
    sum=sum+power
    temp=temp//10
if( sum == n):
    print(f"{n}:{sum} armstrong")
if( sum !=n):
    print(f"{n}:{sum} normal number")