num = 1234
reversed_num = 0
y=num

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: ",reversed_num)
print("Original Number: ", y)