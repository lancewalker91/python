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
        print ("ˮ�������ڹ�%dֻ,С��%dֻ"%(self.t.num,self.f.num))
