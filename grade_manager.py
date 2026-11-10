
# Student Grade Manager

# Store student details
students = []


# Function to calculate grade
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Function to add a student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty!")
        return

    try:
        mark = float(input("Enter student mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100!")
            return

        student = {
            "name": name,
            "mark": mark
        }

        students.append(student)

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter a valid number!")


# Function to display student results
def show_results():
    if len(students) == 0:
        print("\nNo students found! Please add students first.")
        return

    print("\n" + "=" * 40)
    print(f"{'Name':<15}{'Mark':<12}{'Grade':<10}")
    print("=" * 40)

    marks = []

    for student in students:
        name = student["name"]
        mark = student["mark"]
        grade = get_grade(mark)

        marks.append(mark)

        print(f"{name:<15}{mark:<12g}{grade:<10}")

    print("=" * 40)

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Average: {average:.1f}")
    print(f"Highest Mark: {highest:g}")
    print(f"Lowest Mark: {lowest:g}")
    print("=" * 40)


# Main menu
while True:

    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        show_results()

    elif choice == "3":
        print("\nThank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
