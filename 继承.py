# -*- coding: cp936 -*-
import random as r
class Fish:
    def _init_(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -=1
        print ("我的位置是",self.x,self.y)
class Godfish(Fish):
    pass
class crap(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def _init_(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃货的梦想")
            self.hungry = False
        else:
            print("太撑了,吃不下")
            
