weight = int(input('Weight: '))
unit = input('(L)bs or (K)kg: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converte = weight / 0.45
    print(f"you are {converte} lbs")
