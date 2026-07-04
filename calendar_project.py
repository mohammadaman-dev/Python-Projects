import calendar

print("=== CALENDAR PROJECT ===")

year = int(input("Enter Year: "))
month = int(input("Enter Month (1-12): "))

print()
print(calendar.month(year, month))
