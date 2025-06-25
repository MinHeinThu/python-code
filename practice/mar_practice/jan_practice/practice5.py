class Prepend:
    def __init__(self, start):
        self.start = start

    def write(self, word):
        print(self.start + word)
    
p = Prepend('+++ ')
p.write('Hello')

class Rational:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self):
        return (self.x + self.y)
   
r = Rational(1, 4)
print(r.__add__())