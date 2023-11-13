#Accept a positive integer as input and print the sum of the digits in the number.
num=int(input("Enter a positive integer: "))
sum=0
if num>0:
    num=str(num)
    for i in num:
        sum+=int(i)
    print(f"The sum of the digits in number is {sum}")
else:
    print("Enter only positive integers.")