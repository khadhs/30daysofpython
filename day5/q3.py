e1=int(input ("Enter id 1 : "))
e2=int(input ("Enter id 2 : "))
e3=int(input ("Enter id 3 : "))
e4=int(input ("Enter id 4 : "))
e5=int(input ("Enter id 5 : "))
if (e1+e2)%2==0 and (e2+e3)%2 ==0 and (e3+e4)%2==0 and (e4+e5)%2==0 and (e5+e1)%2==0:
    print("Yes.")
else:
    print("No.")