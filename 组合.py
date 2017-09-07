class T:
    def _init_(self,x):
        self.num = x
class F:
    def _init_ (self,x):
        self.num = x
class P:
    def _init_ (self,x,y):
        self.t = T(x)
        delf.f = F(x)
    def print_num(self):
        print ("水池里有乌龟%d只,小鱼%d只"%(self.t.num,self.f.num))
