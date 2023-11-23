even_num = []

for number in range(int(input("Start:")), int(input("End:")) + 1):
    if 0 == number % 2:
        even_num.append(number)

print("Even Number:", even_num)
