# -*- coding: cp936 -*-
import random as r
class Fish:
    def _init_(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -=1
        print ("�ҵ�λ����",self.x,self.y)
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
            print("�Ի�������")
            self.hungry = False
        else:
            print("̫����,�Բ���")
            
