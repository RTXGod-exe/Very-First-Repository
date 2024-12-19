import calendar

def display_calendar():
    print("=" * 100)
    print("Welcome to the Calendar Program!")
    print("=" * 100)

    while True:
        year = int(input("Enter the year (e.g., 2024): "))
        month = int(input("Enter the month (1-12): "))
    
        if 1 <= month <= 12:
           print("\nHere is the calendar:\n")
           print(calendar.month(year, month))
           break
        else:
           print("Invalid month. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    display_calendar()
