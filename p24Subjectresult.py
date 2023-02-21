Mark1 = int(input("Enter the marks in english =>"))
Mark2 = int(input("Enter the marks in maths =>")) 
Mark3 = int(input("Enter the marks in hindi =>"))
total = Mark1+Mark2+Mark3

print("Total = ",total)

if total>90:
    print("Grade: A")
elif total>=50 and total<90:
    print("Grade: B")
else:
    print("Grade: C")