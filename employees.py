
from productivity import ProductivitySystem
from hr import PayrollSystem
from contacts import AddressBook
# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name       

#         # You can now add the Address to the Employee class through composition:
#         self.address = None     
# The Employee class is intialized with the id, name, and address attributes.
# It also requires the productivity role for the employee and the payroll policy.

class Employee:
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll
    def work(self, hours): # The class exposes a .work() method that takes the hours worked.
        duties = self.role.perform_duties(hours)
        self.payroll.track_work(hours)
    def calculate_payroll(self):
        return self.payroll.calculate_payroll() 

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)        
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary        

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked 
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} on the phone.')
class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')                

# class TemporarySecretary(Secretary, HourlyEmployee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super().__init__(id, name, hours_worked, hour_rate)

# temporary_secretary = TemporarySecretary(5, 'Robin Williams', 40, 9)
# print(temporary_secretary)

# You can bypass the MRO by reversing the inheritance order
# and directly calling HourlyEmployee.__init__() as follows:
# class TemporarySecretary(HourlyEmployee, Secretary):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

# class TemporarySecretary(Secretary, HourlyEmployee):
#     pass

# class TemporarySecretary(HourlyEmployee, Secretary):
#     pass 
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

#     def calculate_payroll(self):
#         return HourlyEmployee.calculate_payroll(self)



# class TemporarySecretary(Secretary, HourlyEmployee):
#     def __init__(self, id, name, hours_worked, hour)

class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)


class EmployeeDatabase: # keeps track of all the employees in the company. For each employee, it tracks the id, name, and role.
    def __init__(self): # it has an instance of the ProductivitySystem, the PayrollSystem, and the AddressBook
        self._employees= [{'id':1, 'name': 'Mary Poppins', 'role': 'manager'}, {'id': 2,'name': 'John Smith', 'role': 'secretary' },]
        self.productivity = ProductivitySystem() # these instances are used to create employees.
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()
    
    @property
    def employees(self): # It exposes an .employees property that returns the list of employees. 
        return [self._create_employee(**data) for data in self._employees] # The Employee objects are created in an internal method ._create_employee().
        # Notice that you don't have different types of Employee clases.
        # You just need to implement a single Employee class:

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)
