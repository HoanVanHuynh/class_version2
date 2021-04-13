class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def calculate_payroll(self):
        return 1000000

# The DisgruntledEmployee class doesn't derive from Empoyee, 
# but it exposes the same interface required by the PayrollSystem.
# The PayrollSystem.calculate_payroll() requires a list of objects
# that implement the following interface:
# An id property or attribute that returns the employee's id
