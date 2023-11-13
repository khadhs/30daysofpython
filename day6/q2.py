#Accept a positive integer n as input and print the first n integers on a line separated by a comma.
num=int(input("Enter a positive integer:"))
if num>0:
    for i in range(1,num+1):
        i=str(i)
        print(i,end=',')
