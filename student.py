
class Student:
    """A sample Student class"""

    def __init__(self, firstname, lastname, rollnum):
        self.firstname = firstname
        self.lastname = lastname
        self.rollnum = rollnum

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def __repr__(self):
        return "Student('{}', '{}', {})".format(self.firstname, self.lastname, self.rollnum)
