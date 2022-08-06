num=int(input("Enter the nth term\n"))
num1=0
num2=1
num3=0
print("the sequence is ",num1,num2)
for i in range(0,num):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")
    print()

print("NOTE:- in this program the sequence starts from 0 to nth term, here i am printing 0 and 1 at first that's why they are printer first and then the sequence, those are also the part of the sequence ")
