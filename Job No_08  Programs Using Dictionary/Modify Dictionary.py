person = {
    "name": "Rafi",
    "age": "17+",
    "city": "Savar",
    "email": "mahfuz.rafi2019@gmail.com"
}

print("\nPerson Information:")
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Email:", person["email"])

#Modify information in the dictionary
person["city"] = "Dhaka"
person["email"] = "mahfuz.rafi07@gmail.com"

#print the modified info
print("\nModified Person Dictionary:")
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Email:", person["email"])
