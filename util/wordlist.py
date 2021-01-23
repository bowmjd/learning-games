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

# print(load_wordlist(r'C:\Users\xjxb385\Downloads\Terms-to-Block.csv')[:10])
print(encode('John\'s test'))
print(decode(encode('John\'s test')))