from employee import Employee
from shift import Shift_employee, ShiftCapacityError

def main():
    print("Employee & Shift Management System\n")

    # Create employees
    e1 = Employee(101, "Alice", "Manager")
    e2 = Employee(102, "Bob", "Developer")
    e3 = Employee(103, "Charlie", "Analyst")
    e4 = Employee(104, "Deck", "Software Engineering")
    e5 = Employee(105, "Dev", "HR")

    # Show all employees
    print("All Employees:")
    Employee.show_all()
    print("\n")

    # Create shifts
    morning_shift = Shift_employee("Morning", 2)
    evening_shift = Shift_employee("Evening", 2)

    # Assign employees to Morning shift
    for emp in [e1, e2, e3]:
        try:
            morning_shift.add_shift_employee(emp)
        except ShiftCapacityError as e:
            print(f"⚠️ {e}")

    # Assign employees to Evening shift
    for emp in [e4, e5]:
        try:
            evening_shift.add_shift_employee(emp)
        except ShiftCapacityError as e:
            print(f"⚠️ {e}")

    # Show shift info
    print("\nShifts Info:")
    print(morning_shift)
    print(evening_shift)

if __name__ == "__main__":
    main()
