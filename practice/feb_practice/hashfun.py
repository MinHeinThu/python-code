# Hash function implementation in python using set, dict
# look up, add, remove T: O(1)


from email.policy import default


my_dict = {'Dave': '001', 'Ava': '002', 'Joe': '003'}
print(my_dict)
print(type(my_dict))

new_dict = dict(Dave = '001', ava = '002', Joe = '003')
print(new_dict)
print(type(new_dict))

# hashsets
s = set()
print(s)

# Add item into set - O(1)
s.add(2)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

# Lookup item in the set - O(1)
if 1 in s:
    print(True)
else:
    print(False)

# Remove item from set - O(1)
# if item is not there it will show error
try:
    s.remove(5)
    print(s)
except KeyError:
    print("Key doesn't have in the set")

# Set construction - O(s) - S is the length of the string

string = 'aaaaabbbbbcccccceeeeeee'
sett = set(string) 
print(sett)

# Look over items in set - O(n)
for x in s:
    print(x)

# Hashmaps - Dictionaries

d = {'greg': 3, 'steve': 2, 'rob': 3}
print(d)

# Add the key:val in dictionary: O(1)
d['jack'] = 4
print(d)

# Check for presence of key in dictionary: O(1)

if 'greg' in d:
    print(True)
else:
    print(False)

# Check the value corresponding to a key in the dictionary: O(1)
print(d['greg'])

print(d.get("greg"))

# Looking the key in dict
print(d.keys())

# Looking the val in dict
print(d.values())


# Loop over the key, values in the dictionary: O(n)
for key,val in d.items():
    print(f'key {key}: val {val}')

# Defaultdict
from collections import defaultdict

default = defaultdict(list)
default[2]
print(default)

# Counter
from collections import Counter

print(string)

counter = Counter(string)
print(counter)