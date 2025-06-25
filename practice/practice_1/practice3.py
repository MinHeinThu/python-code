class MathOperations:
    def add(self, *args):
        return sum(args)
obj = MathOperations()
print(obj.add(1,3,4))
