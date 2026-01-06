
from Student_Manager import StudentManager


def display_menu():
    """Display the interactive menu options"""
    print(" Student Management System")
    print("=" * 70)
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. Search by Roll")
    print("5. Search by Name")
    print("6. View All Students")
    print("7. Statistics")
    print("8. Exit Program")
    print("=" * 70)
def get_marks_input() -> list:
    """Prompt user to enter 5 subject marks and return as a list of floats"""
    marks = []
    print("\nEnter marks for 5 subjects (0-100):")
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"  Subject {i} marks: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print(" Enter a valid mark between 0 and 100.")
            except ValueError:
                print(" Invalid input. Enter a number.")
    return marks


def main():
    """Main interactive menu loop"""
    manager = StudentManager()

    print("=" * 70)
    print("Welcome to the Student Management System!")
    print("=" * 70)

    while True:
        display_menu()
        choice = input("\nYour choice (1-8): ").strip()

        if choice == "1":
            # Add Student
            print("\n Adding a student...")
            try:
                roll = int(input("Roll Number: "))
                name = input("Name: ")

                # Marks for 5 subjects
                marks = get_marks_input()

                # Department input with guidance
                print("\nDepartment options:")
                print("  CSE ")
                print("  EEE ")
                print("  BBA ")
                print("  LAW ")
                print("  MATH")
                print("  GENERAL ")
                dept = input("Department (default: GENERAL): ") or "GENERAL"

                result = manager.add_student(
                    roll=roll,
                    name=name,
                    marks=marks,
                    department=dept
                )
                print(result)
            except ValueError:
                print("❌ Error: Please enter valid data!")

        elif choice == "2":
            # Remove Student
            print("\n Removing a student...")
            try:
                roll = int(input("Roll Number to remove: "))
                result = manager.remove_student(roll)
                print(result)
            except ValueError:
                print(" Error: Invalid roll number!")

        elif choice == "3":
            # Update Student
            print("\n Updating a student...")
            try:
                roll = int(input("Roll Number to update: "))
                name = input("New Name (press Enter to skip): ").strip()
                
                marks_input = input("Update marks for 5 subjects? (y/n): ").strip().lower()
                marks = None
                if marks_input == 'y':
                    marks = get_marks_input()

                print("\nDepartment options:")
                print("  CSE, EEE, BBA, LAW, MATH, GENERAL")
                dept = input("New Department (press Enter to skip): ").strip()

                update_fields = {}
                if name:
                    update_fields["name"] = name
                if marks:
                    update_fields["marks"] = marks
                if dept:
                    update_fields["department"] = dept

                result = manager.update_student(roll, **update_fields)
                print(result)
            except ValueError:
                print("Error: Invalid input!")

        elif choice == "4":
            # Search by Roll
            try:
                roll = int(input("Enter Roll Number to search: "))
                print(manager.search_student(roll))
            except ValueError:
                print("Error: Invalid roll number!")

        elif choice == "5":
            # Search by Name
            name = input("Enter full name to search: ").strip()
            print(manager.search_by_name(name))

        elif choice == "6":
            # View All Students
            print(manager.get_all_students())

        elif choice == "7":
            # Statistics
            print(manager.get_statistics())

        elif choice == "8":
            # Exit
            print("\n🚪 Exiting Student Management System. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
