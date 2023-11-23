with open("Read Write And Print.txt", "w") as file:
    show = file.write("Hello Everyone,Hope You Are Well")

with open("Read Write And Print.txt", "r") as file:
    show = file.read()

print(show)
