try:
    name = input("Enter student name: ")

    marks = int(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100")

except ValueError as e:
    print("Error:", e)

else:
    print("\nStudent Details")
    print("Name:", name)
    print("Marks:", marks)

    if marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")

finally:
    print("\nProgram Completed")
