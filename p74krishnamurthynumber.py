import math
number=int(input("Enter the number to check krishnamurthy number =>"))
temp = number
sum = 0
while temp >0:
    rem = temp%10
    fact = math.factorial(rem)
    sum = sum+fact
    temp=temp//10
if sum==number:
    print("No is a krishnamurthy number")
else:
    print("No is not a krishnamurthy number")    