from todo_app.bonus.converter14 import convert
from todo_app.bonus.parsers14 import parse
# created with move and create a new file using pycharm refactor option when highlighting the function

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")
if result < 1:
    print("Kid is too short")
else:
    print("Kid can use the slide")