even_numbers = []
for number in range(int(input("Start: ")), int(input("End: ")) + 1):
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)
