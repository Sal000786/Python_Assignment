from re import I


num=int(input("enter a numer"))
sum=0
sum2=0
for i in range(num):
    if(i%2==0):
        sum+=i 
    if(i%2!=0):
        sum2+=i
print("sum of all the odd rumbers are\n",sum2)
print("sum of all the even number are \n",sum)
