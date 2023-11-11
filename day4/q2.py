#Create a program that checks if a given year is a century year (ending in 00) or not.
year=input("Enter a year:")
list=[]
for i in year:
    list.append(i)
if list[-2]=='0' and list[-1] =='0':
    print("the given year is a century year")
else:
    print("the given year is not a century year")

