class Student:
    """Student class defines common information for all students"""

    def __init__(self, first="", last="", major='CIS'):
        self.fname = first
        self.lname = last
        self.major = major

    @property
    def fname(self):
        return self.__fname.capitalize()

    @fname.setter
    def fname(self, first):
        if first.isalpha():
            self.__fname = first
        else:
            self.__fname = 'Unknown'

    @property
    def lname(self):
        return self.__lname.capitalize()

    @lname.setter
    def lname(self, last):
        if last.isalpha():
            self.__lname = last
        else:
            self.__lname = 'Unknown'

    @property
    def major(self):
        return self.__major.upper()

    @major.setter
    def major(self, major):
        if major.isalpha() and len(major) == 3:
            self.__major = major

    def __str__(self):
        """Override the string representation of a student"""
        # Use the properties or you are not executing the formatting
        return f'{self.lname}, {self.fname} - {self.major}'


class GradStudent(Student):
    """GradStudent inherits from Student to get first & last name"""
    def __init__(self, thesis, first="", last='', major='CIS'):
        """Initialize a GradStudent with first name and thesis"""
        super().__init__(first, last, major)
        self.thesis = thesis

    @property
    def thesis(self):
        return self.__thesis.capitalize()

    @thesis.setter
    def thesis(self, new_thesis):
        """Add Thesis label to entry"""
        self.__thesis = 'Thesis: ' + new_thesis

    def __str__(self):
        """Override the string representation of a student"""
        stu_info = super().__str__()
        return f'{stu_info}  {self.thesis}'


