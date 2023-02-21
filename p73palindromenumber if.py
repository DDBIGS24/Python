num = 121
reversed_num = 0
y=num

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: ",reversed_num)
print("Original Number: ", y)

if y==reversed_num:
    print("the numebr is palindrome number")
else:
    print("the number is not palidrome number")    