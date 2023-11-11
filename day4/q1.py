# Write a program that takes three integer inputs representing the lengths of the sides of a triangle. 
# Your task is to determine and display the type of the triangle: equilateral, isosceles, or scalene.
s1=int(input("enter the 1st side: "))
s2=int(input("enter the 2nd side: "))
s3=int(input("enter the 3rd side: "))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    if s1==s2==s3:
        print("it is an equilateral triangle")
    elif s1!= s2!=s3:
        print("it is a scalene triangle.")
    else:
        print("it is an isosceles triangle.")
else:
    print("The given sides doesn't form a triangle")
