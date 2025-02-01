# Assignment


from tabulate import tabulate
from abc import ABC, abstractmethod
class Employee(ABC):
    man_list = {}
    dev_list = {}
    emp_list = {}
    @abstractmethod
    def work():
        pass
    @abstractmethod
    def get_salary():
        pass
class Manager(Employee):
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
        Manager.man_list[name] = salary
    def work(self):
        return "Keep track of the assigned project and team members"
    def get_salary(self, name):
        return Manager.man_list[name]
class Developer(Employee):
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
        Manager.dev_list[name] = salary
    def work(self):
        return "Develop assigned code"
    def get_salary(self, name):
        return Developer.dev_list[name]
class Department():
    def hire(self, employee, salary):
        self.employee = employee
        self.salary = salary
        Employee.emp_list[employee] = salary
        print("Employee added!")
    def fire(self, employee):
        del Employee.emp_list[employee]
        print("Employee removed!")
    def get_total_salary(self):
        ans = 0
        for val in Employee.emp_list.values():
            ans += val
        for val in Employee.dev_list.values():
            ans += val
        for val in Employee.man_list.values():
            ans += val
        print(ans)
    def show_employee_details(self):
        Employee.emp_list = Manager.man_list | Developer.dev_list | Employee.emp_list
        print(tabulate(Employee.emp_list.items(), headers=["Employee", "Salary"], tablefmt="grid"))
        # for key, val in Employee.emp_list.items():
        #     print(key, val)

man1 = Manager("Manager1", 230000)
# print(man1.get_salary("Manager1"))
man2 = Manager("Manager2", 450000)
# print(man2.get_salary("Manager2"))
print(Manager.man_list)

dev1 = Developer("Developer1", 180000)
# print(dev1.get_salary("Developer1"))
dev2 = Developer("Developer2", 330000)
# print(dev2.get_salary("Developer2"))
print(Developer.dev_list)

dep1 = Department()
dep1.hire("Emp1", 450000)
dep1.get_total_salary()
dep1.fire("Emp1")
dep1.show_employee_details()
print(f'Total salary expense: {sum(Employee.emp_list.values())}')