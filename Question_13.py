
import cmath
a=int(input("Enter a number\n"))
b=int(input("Enter a number\n"))
c=int(input("Enter a number\n"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("the solution are",(sol1,sol2))