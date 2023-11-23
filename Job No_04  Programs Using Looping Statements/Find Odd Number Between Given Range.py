obb_numbers = []
for number in range(int(input("Start: ")), int(input("End: ")) + 1):
    if number % 2 != 0:
        obb_numbers.append(number)
print(obb_numbers)
