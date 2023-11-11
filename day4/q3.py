#Design a program that calculates the roots of a quadratic equation given its coefficients (a, b, and c)
#( Hint: discriminant = b**2 - 4 * a * c)**
import math
a= int (input ("Enter the co eff. of a: "))
b= int (input ("Enter the co eff. of b: "))
c= int (input ("Enter the co eff. of c: "))
discriminant= b**2 - 4*a*c
if discriminant<0:
    discriminant*=-1
root1= (-b+ math.sqrt(discriminant))/2*a
root2= (-b - math.sqrt(discriminant))/2*a
print("The roots of the equation are:",root1,"and",root2)