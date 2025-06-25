def add_numbers(*args):
    return sum(args)

print(add_numbers(3,2))

def info(**kwargs):
    print(kwargs['name'])

info(name='Jack')

hell = {'name': "min", 'age': 22}
del hell['name']
print(hell)

print(type(hell))