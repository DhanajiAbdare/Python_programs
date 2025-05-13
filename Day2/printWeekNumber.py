def get_week_number(week_name):
    week_dict = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }
    return week_dict.get(week_name.capitalize(), "Invalid week name")

# Taking user input
week_name = input("Enter the name of the week: ")
week_number = get_week_number(week_name)

# Printing the result
print(f"The week number for {week_name} is: {week_number}")

