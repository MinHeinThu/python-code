def word_count(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        word = ''.join([c for c in word if c.isalnum()])
        if word in counts:
            counts[word] = counts.get(word, 0) + 1
        else:
            counts[word] = 1
    return counts
text = "This is a test string. This string has some 11repeated words."
counts = word_count(text)
print(counts)

def unique_characters(text):
    # Your code here
    sett = set()
    for c in text:
        sett.add(c)
    return sett

text = "hello"
unique = unique_characters(text)
print(unique)  # Expected output: {'h', 'e', 'l', 'o'}

def find_duplicates(lst):
   # Your code here
    sett = set()
    count = {}
    for i in lst:
        if i in count:
            count[i] = count.get(i, 0) + 1
        else:
            count[i] = 1
    for key, val in count.items():
        if val > 1:
            sett.add(key)
    return sett
    
my_list = [1, 2, 3, 2, 4, 1, 5, 3]
duplicates = find_duplicates(my_list)
print(duplicates)  # Expected output: {1, 2, 3}