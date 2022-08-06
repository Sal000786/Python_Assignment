import sys
class salman:
    def sal():
        
        num1=1
        while(True):
            num2=input("enter done to exit\n")
            if num2=="done":
                break
            # num2=int(input("enter a number to check whether its a larger or not\n"))
            num3=int(num2)
            if(num3>num1):
                print("the number 2 is greater\n")
            else:
                print("the number 1 is greater")
            num1=num3+num1
    salman=sal()
