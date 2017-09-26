import unittest,my_path
class ProductTest(unittest.TestCase):
    def testintegers(self):
        for x in range(-10,10):
            for y in range(-10,10):
                p = my_path.product(x,y)
                self.failUnless(p == x*y,'失败')
    def testFloats(self):
        for x in range(-10,10):
            for y in range(-10,10):
                x = x/10.0
                y = y/10.0
                p = my_path.product(x,y)
                self.failUnless(p == x*y,'float shibai')
if __name__ == '__main__':unittest.main()

