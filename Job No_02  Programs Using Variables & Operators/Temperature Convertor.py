temp = float(input('Please Enter Your Temperature: '))
unit = input("It's (C)celsius or (F)fahrenheit: ")


if unit.upper() == "C":
    converted = temp*9 / 5 + 32
    print(f"Temperature is {converted}° Fahrenheit")
elif unit.upper() == "F":
    converte = (temp - 32) * 5 / 9
    print(f"Temperature is {converte}° Celsius")

else:
    print('Sorry,You type the wrong word')
