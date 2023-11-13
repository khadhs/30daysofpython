# Accept two positive integers a and b as input. Print the sum of all integers in the range [1000, 2000],
# endpoints inclusive, that are divisible by both a and b. 
# If you find no number satisfying this condition in the given range, then print 0. (30 Points)
a=int(input("Enter a positive integer:"))
b=int(input("Enter a positive integer:"))
list=[]
for i in range(1000,2001):
    if i%a==0 and i%b==0:
        list.append(i)
sum=0
for i in list:
    sum+=i
print("The sum of the integers is:",sum)
if len(list)<1:
    print('0')   
        
    


