class Employee:
    employees = []  ## class-level list to store all employees
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        Employee.employees.append(self)  # add each new employee automatically
    
    @staticmethod
    def header():
        return f"{'Employee ID':<12} | {'Name':<10} | {'Role':<10}"
    
    def __str__(self):
        return f"{self.emp_id:<12} |  {self.name:<10} | {self.role:<10}"

    @classmethod
    def show_all(cls):
        print(cls.header())
        print("-" * 36)
        for emp in cls.employees:
            print(emp)    