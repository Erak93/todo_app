from todo_app.bonus.bonus14 import feet_inches


def parse(feet_inchese):
    parts = feet_inches.split(" ")  # splits at the space
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet":feet, "inches":inches}
