#!/usr/bin/python3 
# Change the above path to the path where python3 is stored on your machine. (Tip: type "which python3" into your shell)
# Do NOT remove the "#!"

# Requires Python 3.10+

from datetime import datetime, timedelta

firstdate_filename = "date_firstday.txt" # You can change this to whatever name you like
date_format = "%d-%m-%Y"                 # You can change this to whatever format you like

# Some base functions
def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, date_format)

def tostring_date(date_obj: datetime) -> str:
    if date_obj is None:
        return "date_obj is None"
    return date_obj.strftime(date_format)

def getWeekday(date_obj: datetime) -> str:
    return date_obj.strftime("%A")

def validate_parse_date(date_str: str, date_obj: list=[None]) -> bool:
    """
    If date_str is invalid, returns False. 
    If date_str is valid, assigns parse_date(date_str) to date_obj and returns True.

    Parameters:
        date_str (str): A date
        date_obj (list): A list that should hold a single element of None. If given, it will be populated with a datetime object, which is parsed from the given date_str.

    Returns:
        bool: Whether date_str is in a valid format according to strptime() in parse_date().
    """
    try:
        date_obj[0] = parse_date(date_str)
        return True
    except:
        return False



def getWeekFromDate(date: datetime) -> int:
    return ((date - firstdate).days // 7) + 1

def getDateFromWeekAndDay(week: int, day: int) -> datetime:
    return firstdate + timedelta(days = (week-1)*7+day-1)



def displayMenu() -> None:
    print("""\n  ~~ Main menu ~~\n
  1> Edit firstdate value
  2> Convert: date         -> week
  3> Convert: week and day -> date
  0> Quit\n""")

def editFirstDate() -> None:
    firstdate_str = tostring_date(firstdate)
    while True:
        print("\nCurrently, the firstdate value is " + firstdate_str + ".")
        new_firstdate_str = input("Enter new firstdate value in DD-MM-YYYY format (leave blank to cancel): ")
        if new_firstdate_str == "":
            print("\nCancelled.")
            break
        if not validate_parse_date(new_firstdate_str):
            print("\nInvalid date format. Please try again.")
            continue

        while True:
            confirm = input(f"Confirm that new firstdate is {new_firstdate_str}? (y/n) ")
            if confirm.strip().lower() == "y":
                # User has provided a correctly formatted date and confirmed the edit - edit is gone through with, operation is completed.
                with open(firstdate_filename, "w") as f:
                    f.write(new_firstdate_str)
                with open(firstdate_filename, "r") as f:
                    print(f"\nSuccessfully modified. New firstdate value: {f.read()}")
                return
            elif confirm.lower() == "n":
                # User cancels the operation.
                print("\nSuccessfully cancelled. You may now enter the new firstdate again.")
                break
            else:
                print("\nInvalid selection. Please try again.")

def checkWeekNumber() -> None:
    while True:
        print("\nCheck week number from a given date.")
        date_str = input("Enter a date in the DD-MM-YYYY format (leave blank to quit): ")
        if date_str == "":
            return

        date_obj = [None]
        if not validate_parse_date(date_str, date_obj):
            print("\nInvalid date format. Please try again.")
            continue
        date_obj = date_obj[0] # Assign the datetime object contained in the list that is date_obj, to itself, so now date_obj is a datetime object instead of a list.
        with open(firstdate_filename, "r") as f:
            firstdate: datetime = parse_date(f.read())
            if date_obj < firstdate:
                f.seek(0) # Reset the file pointer to the beginning 
                print(f"\nDate out of range: Given date should be later than or equal to the first day of the semester, which is currently set to: {f.read()}")
                continue
        weeknum: int = getWeekFromDate(date_obj)
        print(f"\n{date_str} is a {getWeekday(date_obj)} in Week {weeknum}.")

        again = input("Again? y for yes, anything else to quit: ")
        if again.lower() != "y": 
            return
    
def checkDateFromWeekAndDay() -> None:
    print("\nType a week number and a day number (1 for Monday, 7 for Sunday), converts to a date.")
    while True:
        week = input("Enter week number (leave blank to quit): ")
        if week == "":
            return
        if not week.isdigit():
            print("\nInvalid input - not a number.")
            continue
        week = int(week)

        while True:
            day = input("Enter a day number (1 for Monday, 7 for Sunday): ")
            if not day.isdigit() or int(day)<1 or int(day)>7:
                print("\nInvalid input - not a number or out of range.")
                continue
            break
        day = int(day)

        date_obj: datetime = getDateFromWeekAndDay(week, day)
        date_str = tostring_date(date_obj)
        print(f"\nWeek {week}, Day {day}\n{date_str}, {getWeekday(date_obj)}\n")


def main() -> None:
    while True:
        displayMenu()
        while True:
            option = int(input("Enter option: "))
            if not option.isdigit():
                print("\nInvalid option. Please try again.")
                continue
            option = int(option)

            if option == 0:
                print("Quitting DateWeekConverter made by cookie. Have a nice day :3")
                return
            if not (option >= 1 and option <= 3):
                print("\nInvalid option. Please try again.")
                continue            
            break

        # print() # Print an empty line
        match option:
            # Edit firstdate value
            case 1:
                editFirstDate()  
            # Check week number of given date      
            case 2:
                checkWeekNumber()
            # Calculate date from given week number and day number
            case 3:
                checkDateFromWeekAndDay()

# Check if file that stores date of first day of semester exists.
try:
    # If file exists, read first date.
    with open(firstdate_filename, "r") as f:
        firstdate: datetime = parse_date(f.read())
except FileNotFoundError:
    # If file doesn’t exist, create it and prompt user to input first date.
    with open(firstdate_filename, "w") as f:
        firstdate_str = input("You haven't set the first day of the semester yet. Please enter the date of the first day of your semester (i.e. Monday of Week 1) in the format DD-MM-YYYY: ")
        f.write(firstdate_str)
        firstdate: datetime = parse_date(firstdate_str)

# Start main program
main()

