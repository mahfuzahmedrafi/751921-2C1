odd_num = []

for number in range(int(input("Start:")), int(input("End:")) + 1):
    if 0 == number % 2:
        odd_num.append(number)

print("Odd Number:", odd_num)
