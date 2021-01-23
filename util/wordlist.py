# wordlist.py
# Create and save master word list.

# encode(s)
# Apply simple shift cipher with offset to string s
def encode(s, offset=5):
    output = ''
    for char in s:
        num = ord(char)
        if num >= 65 and num <= 90:
            num = ((num + offset - 65) % 26) + 65
        elif num >= 97 and num <= 122:
            num = ((num + offset - 97) % 26) + 97            
        output += chr(num)
    return output

# decode(s)
# Decode simple shift cipher with offset to string s
def decode(s, offset=5):
    return encode(s, -5)

# load_wordlist(filepath)
# Read wordlist from a file (comma delimited)
def load_wordlist(filepath):
    list = []
    f = open(filepath, 'r')
    for line in f:
        word = line.split(',')[0].strip().replace('"', '')
        list += [word]
    return list

# union(list1, list2)
# Return the union of two wordlists.
# If sort_before_merge=True, sort and dedup prior to merging.
# Otherwise assume the lists are sorted and deduped.
def union(list1, list2, sort_before_merge=True):
    if sort_before_merge:
        list1 = sorted(set(list1))
        list2 = sorted(set(list2))
    i = 0
    j = 0
    output = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            output += list1[i]
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            output += list1[i]
            i += 1
        else:
            output += list2[j]
            j += 1
    if i == len(list1):
        output += list2[j:]
    if j == len(list2):
        output += list1[i:]
    return output

# intersect(list1, list2)
# Return the intersection of two wordlists.
# If sort_before_merge=True, sort and dedup prior to merging.
# Otherwise assume the lists are sorted and deduped.
def intersect(list1, list2, sort_before_merge=True):
    if sort_before_merge:
        list1 = sorted(set(list1))
        list2 = sorted(set(list2))
    i = 0
    j = 0
    output = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            output += list1[i]
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return output

# diff(list1, list2)
# Return the difference of two wordlists (union minus intersection).
# If sort_before_merge=True, sort and dedup prior to merging.
# Otherwise assume the lists are sorted and deduped.
def diff(list1, list2, sort_before_merge=True):
    if sort_before_merge:
        list1 = sorted(set(list1))
        list2 = sorted(set(list2))
    i = 0
    j = 0
    output = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            output += list1[i]
            i += 1
        else:
            output += list2[j]
            j += 1
    if i == len(list1):
        output += list2[j:]
    if j == len(list2):
        output += list1[i:]
    return output

# print(load_wordlist(r'C:\Users\xjxb385\Downloads\Terms-to-Block.csv')[:10])
# print(encode('John\'s test'))
# print(decode(encode('John\'s test')))

a = ['a', 'b', 'c']
b = ['b', 'c', 'd', 'e']
c = []
d = []
print(union(a, b))
print(union(b, a))
print(intersect(a, b))
print(intersect(b, a))
print(union(a, c))
print(union(c, a))
print(intersect(a, c))
print(intersect(c, a))
print(diff(a, b))
print(diff(b, a))
print(diff(a, c))
print(diff(c, a))
print(union(c,d))
print(intersect(c, d))
print(diff(c, d))