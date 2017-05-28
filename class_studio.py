# class Rectangle:
#     '''Rectangle class takes two ints (width and length) and creates rectangle'''
#     def __init__(self, width=5, length=5):
#         self.width = width
#         self.length = length

#     def __str__(self):
#         return "I'm a rectangle. My length is {} and width is {}".format(self.length, self.width)

#     def area(self):
#         return self.width * self.length

#     def perimeter(self):
#         return self.width * 2 + self.length * 2

#     def is_smaller(self, rect):
#         return self.area() < rect.area()

#     def is_square(self):
#         return self.width == self.length



# my_rectangle = Rectangle(10, 5)
# my_other_rectangle = Rectangle()
# my_area = my_rectangle.area()
# print(my_area)
# print(my_rectangle.perimeter())
# print(my_rectangle.is_smaller(my_other_rectangle))
# print(my_rectangle.is_square())

class BaseballPlayer:
    '''create a baseball player taking in a name, number and style of hitting'''
    def __init__(self, name, number, hitside):
        self.name = name
        self.number = number
        self.hitside = hitside
        self.totalhits = 0
        self.totalrbi = 0
        self.totalgames = 0
    
    def __str__(self):
        '''give a players stats when printing'''
        return "Player: {} has {} total hits and {} RBI's out of {} total games played".format(self.name, self.totalhits, self.totalrbi, self.totalgames)

    def game(self, hits, rbi):
        '''takes an integer for hits and and integer for RBI's and adds them to lifetime stats'''
        self.totalhits += hits
        self.totalrbi += rbi
        self.totalgames += 1

player1 = BaseballPlayer("Bob", 1, "Right")
player1.game(2, 1)
player1.game(3, 2)
player1.game(1, 1)
player1.game(3, 1)
print(player1)



