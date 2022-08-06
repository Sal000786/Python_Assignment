num=int(input("enter a number to check whether it's a prime number or not\n"))
for i in range(2,num+1):
    if(num%i==0):
        print("it's not a prime number")
        break

    else:
        print("it's a prime number")
        break