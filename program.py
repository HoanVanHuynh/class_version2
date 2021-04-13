import hr
import employees
import disgruntlet
import productivity
import contacts

# salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = employees.HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = employees.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# dis = disgruntlet.DisgruntledEmployee(5, 'hoan')
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee,
#     dis
# ])




# manager = employees.Manager(1, 'Mary Poppins', 3000)
# manager.address = contacts.Address( '67 Paperwork Ave.',  'Manchester',  'NH',  '03101')
# secretary = employees.Secretary(2, 'Jhon', 1500)
# secretary.address = contacts.Address(
#     '121 Admin Rd', 
#     'Concord', 
#     'NH', 
#     '03301'
# )
# sales_guy = employees.SalesPerson(3, 'Kevein Bacon', 1000, 250)
# factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)
# temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)

# employees = [ manager, secretary, sales_guy, factory_worker, temporary_secretary,]

# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(employees, 40)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees)





# CUSTOMIZING BEHAVIOR WITH COMPOSITION 
# If your design relies on inheritance, you need to find a way
# to change the type of an object to change its behavior.
from hr import PayrollSystem, HourlyPolicy
from productivity import ProductivitySystem
from employees import EmployeeDatabase 

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees
manager = employees[0]
manager.payroll = HourlyPolicy(55)
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)