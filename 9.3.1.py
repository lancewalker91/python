def checkIndex(key):
    """所给的键是能接受的索引吗?

       为了能被接收,键应该是一个非负整数."""
    if not isinstance(key,(int,long)):
        raise TypeError
    if key < 0:
        raise IndexError
class ArithmeticSquence:
    def __init__(self,start=0,step=1):
        """初始化算数序列
        起始值-----序列的第一个值"""
        self.start=start
        self.step=step
        self.changed={}
    def __getitem__(self,key):
        """
        get an item from the arith ."""
        checkIndex(key)

        try:return self.changed[key]
        except KeyError:
            return self.stsrt + key*self.step
    def __setitem__(self,key,value):
        """修改算术序列中的一个项"""
        checkIndex(key)
        sef.changed[key] = value
