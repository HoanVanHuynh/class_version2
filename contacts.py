class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)

# address = Address('55 Main St.', 'Concord', 'NH', '03301')
# print(address)

class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
            2: Address('67 Paperwork Ave', 'Manchester', 'NH', '03101'),
            3: Address('15 Rose St', 'Concord', 'NH', '03301', 'Apt. B-1'),
            4: Address('39 Sole St.', 'Concord', 'NH', '03301'),
            5: Address('99 Mountain Rd.', 'Concord', 'NH', '03301'),
        }
    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address

# The AddressBook class keeps an internal database of Address objects for each employee.
# It exposes a get_employee_address() method
# that returns the address of the specified employee id.
# If the employee id doesn't exist, then it raises a ValueError.
# The Address class implementation remains the same as before:
# The class manages the address components and provides a pretty representation of an address.
# So far, the new classes have been extended to support more funtionality,
# but there are no significant changes to the previous design.
# This is going to change with the design of the employees module and its classes.
# You can start by implementing an EmployeeDatabase class:
