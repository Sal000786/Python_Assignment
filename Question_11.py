num=int(input("Enter a number to check arithmetic exception\n"))
try:
    num=num/0
except ZeroDivisionError as a:
    print("Arithmetic exception caught")
    print(a)
else:
    print(num)