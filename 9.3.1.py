def checkIndex(key):
    """�����ļ����ܽ��ܵ�������?

       Ϊ���ܱ�����,��Ӧ����һ���Ǹ�����."""
    if not isinstance(key,(int,long)):
        raise TypeError
    if key < 0:
        raise IndexError
class ArithmeticSquence:
    def __init__(self,start=0,step=1):
        """��ʼ����������
        ��ʼֵ-----���еĵ�һ��ֵ"""
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
        """�޸����������е�һ����"""
        checkIndex(key)
        sef.changed[key] = value
