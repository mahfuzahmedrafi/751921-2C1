num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    max_number = num1
elif num2 >= num1 and num2 >= num3:
    max_number = num2
else:
    max_number = num3

print(f"The maximum number is: {max_number}")
