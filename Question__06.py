num=float(input("Enter a number between 0.0 to 1.0\n"))
if(num<=1.0):
    if(num>=0.9):
        print("your grade is A")
    elif(num>=0.8):
        print("your grade is B")
    elif(num>=0.7):
        print("your grade is C")
        
    elif(num>=0.6):
        print("your grade is D")
    elif(num<0.6):
        print("sorry you're failed!!")

    
else:
    print("Error occured!!, samller number please")