from random import randint
class Fish:
    def __init__(self):
        self.x = randint(0,10)
        self.y = randint(0,10)
    def move(self):
        self.x -=1
        print('我的位置是:',self.x,self.y)
class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salom(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('吃货次好次火车')
        else:
            print('太撑了')

