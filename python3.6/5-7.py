class Bird:
    def __init__(self):
        self.Hungry = True
    def eat(self):
        if self.Hungry:
            print('Aaaaah.....')
            self.Hungry = False
        else:
            print('No,Thanks')
class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squakk!'
    def sing(self):
        print(self.sound)
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
