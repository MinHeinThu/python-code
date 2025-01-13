# class Parent:

#     #constructor
#     def __init__(self,greeting):
#         self.greeting = greeting
    
#     def respond(self):
#         print(self.greeting)


# greet = Parent("Hello? World!")

# greet.respond()


# # Class
# class Person:

#     # Instance Constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age}"
    
#     # Object Methods
#     def myfunc(self):
#         print("hello My name is {0}".format(self.name))


# # Object
# p1 = Person("Min", 22)
# p1.myfunc()

# p2 = Person("Hein", 23)
# p1.age = 40
# print(p1.age)
# del p1.age

# Perent class
class Person:
    # constructor attribute
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

# Child class
class Student(Person):
    def __init__(self, fname,mname, lname):
        #To keep the inheritance of the parent's __init__ function, 
        # add a call to the parent's __init__() funciton
        #Person.__init__(self, fname, lname)
        # Python also has a super( ) function that make the child class inherit
        # all the methods and properties form its parent
        super().__init__(fname, lname)
        self.mname = mname
    

    # Adding mehhods

    def request(self):
        print(f'love {self.fname + self.mname + self.lname}')
    
    def __str__(self):
        return self.fname + self.mname + self.lname 
p1 = Person("Min","Heinthu")
p1.printname()
s1 = Student("people", "code", "python")
print(s1)
s1.request()


mytuple = (1,3,4)
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))