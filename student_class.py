class Student:
    '''create a student object after getting a name and ID#'''
    def __init__(self, name, identification):
        self.name = name
        self.identification = identification
        self.credits = 0
        self.gpa = 0

    def course(self, credits_earned, gpa_earned):
        '''when student takes a course record credits earned and gpa taken in as integers'''
        self.gpa += gpa_earned
        self.credits += credits_earned

    def standing(self):
        '''return current highschool class standing based on amount of credits taken'''
        if self.credits <= 48:
            class_year = "Freshman"
        elif self.credits > 48 and self.credits <= 96:
            class_year = "Sophomore"
        elif self.credits > 96 and self.credits <= 144:
            class_year = "Junior"
        else:
            class_year = "Senior"
        return class_year

    def __str__(self):
        return "{} is currenty a {} with a {} GPA".format(self.name, self.standing(), self.gpa)


class Course:
    '''Course has number of seats, roster of students, can add/drop students.
     Reports avg GPA of students enrolled'''
    def __init__(self, seats):
        self.openseats = seats
        self.roster = []

    def add_student(self, name):
        if len(self.roster) < self.openseats:
            self.roster.append(name)
            self.openseats -= 1
        else:
            print("Sorry this class is full")

    def drop_student(self, name):
        self.roster.pop()

    def report_gpa(self):
        gpa = 0
        for student in self.roster:
            gpa += student.gpa
        return gpa / len(self.roster)


mike = Student("Mike", 12345)
jill = Student("Jill", 2)

print(mike)
print(jill)

