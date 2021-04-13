class ProductivitySystem:

    def __init__(self):
        self._roles = {'manager': ManagerRole, 'secretary': SecretaryRole,}

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()


    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('-------------')
        for employee in employees:
            employee.work(hours)
        print('')

class ManagerRole:
    def perform_duties(self, hours):
        return f'screams and yells for {hours} hours.'
class SecretaryRole:
    def perform_duties(self, hours):
        return f'does paperwork for {hours} hours.'
class SalesRole:
    def perform_duties(self, hours):
        return f'expends {hours} hours on the phone.'      
class FactoryRole:
    def perform_duties(self, hours):
        return f'manufactures gadgets for {hoous} hours.'  

# Each of the roles you implemented expose a .perform_duties() that
# takes the number of hours worked.
# The methods return a string representing the duties.

# The role classes are independent of each other, but they expose
# the same interface so they are interchangeable.

# you will see later how they are used in the application.                
# The class tracks employees in the track() method that
# takes a list of employees and the number of hours to track.#
# You can now add the productivity system to your program:
