def main():
    meal = input("What's the time? ")
    meal_time = convert(meal)

    if 7 <= meal_time <= 8:
        print("Breakfast time")
    elif 12 <= meal_time <= 13:
        print("Lunch time")
    elif 18 <= meal_time <= 19:
        print("Dinner time")

def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60

main()