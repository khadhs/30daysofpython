#Write a python program that accepts two positive integers $x$ and $y$ as input. Print the number of digits in $x^y$.
x=int(input("Enter the first positive integer:"))
y=int(input("Enter the second positive integer: "))
if x<0 or y<0:
        print("Invalid Input.Enter only positive numbers.")
else:
        a=str(x**y)
        count=0
        for i in a:
            count+=1
        print(count)


