# **You have `n` gold coins with you. You wish to divide this among three of your friends
# under the following conditions:**
# 1. **All three of them should get a non-zero share.**
# 2. **No two of them should get the same number of coins.**
# 3. **You should not have any coins with you at the end of this sharing process.**
# **The input has four lines. The first line contains the number of coins with you.
# The next three lines will have the share given to your three friends. 
# All inputs shall be non-negative integers. 
# If the division satisfies these conditions, then print the string `FAIR`. If not, print `UNFAIR`.**
coins=int(input("Enter the number of coins you have:"))
f1=int(input("Enter the number of coins you give to friend 1: "))
f2=int(input("Enter the number of coins you give to friend 2: "))
f3=int(input("Enter the number of coins you give to friend 3: "))
if f1>=0 and f2 >=0 and f3>=0:
    if f1 % 10!= 0 and f2 % 10!= 0 and f3 % 10!= 0:
        if (f1!=f2!=f3) and (coins-f1-f2-f3 == 0):
                print("Fair")
        else:
             print("Unfair")
    else:
        print("Unfair")
else:
     print("Give only non-negative integers")