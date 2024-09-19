feet_inches = input("Enter feet and inches: ")

def parse(feet_inchese):
    parts = feet_inches.split(" ")  # splits at the space
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet":feet, "inches":inches}

def convert(feet,inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters



parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")
if result < 1:
    print("Kid is too short")
else:
    print("Kid can use the slide")