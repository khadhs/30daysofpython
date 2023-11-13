#Accept a positive integer n as input and print all the factors of n, one number on each line.
num=int(input("Enter a positive integer:"))
if num>0:
    fact=[]
    for i in range(1,num+1):
        if num%i==0:
            fact.append(i)
    for n in fact:
        print (n)     

else:
    print("Enter only positive integers.")