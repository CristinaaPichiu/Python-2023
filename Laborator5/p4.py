class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def assign_tasks(self):
        return "Assign tasks to subordinates"

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, project):
        super().__init__(name, employee_id, salary)
        self.project = project

    def code(self):
        return "Write code for the project"

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id, salary)
        self.sales_target = sales_target

    def meet_target(self):
        return "Meet the sales target"

# Example usage:
if __name__ == "__main__":
    manager = Manager("Alice", 1001, 60000, "Operations")
    print(f"Manager's department: {manager.department}")
    print(manager.assign_tasks())

    engineer = Engineer("Bob", 2005, 75000, "Product Development")
    print(f"Engineer's project: {engineer.project}")
    print(engineer.code())

    salesperson = Salesperson("Charlie", 3003, 50000, 1000000)
    print(f"Salesperson's sales target: {salesperson.sales_target}")
    print(salesperson.meet_target())
