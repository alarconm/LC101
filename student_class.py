class Student:
    '''create a student object after getting a name and ID#'''
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.credits = 0
        self.gpa = 0

    def course(self, credits, gpa):
        '''when student takes a course record credits earned and gpa taken in as integers'''
        self.gpa += gpa
        self.credits += credits

    def standing(self):
        if self.credits <= 48:
            standing = "Freshman"
        elif self.credits > 48 and self.credits <= 96:
            standing = "Sophomore"
        elif self.credits > 96 and self.credits <= 144:
            standing = "Junior"
        else:
            standing = "Senior"
        
        print("{} is currenty a {} with a {} GPA".format(self.name, self.standing, self.gpa))

mike = Student("Mike", 12345)
jill = Student("Jill", 2)

