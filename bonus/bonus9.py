password = input("Enter a new password: ")
result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["upper-case"] = upper

print(result)

if all(result.values()) == True:
    print("Strong password")
else:
    print("Weak password")