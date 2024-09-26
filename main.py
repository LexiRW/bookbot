with open("books/frankenstein.txt") as fp:
    Lines = fp.read()

# words = Lines.split()
# print(len(words))

lower = Lines.lower()

letters = ['a','b','c','d','e','f','g',
           'h','i','j','k','l','m','n',
           'o','p','q','r','s','t','u',
           'v','w','x','y','z']

count = {}

for letter in letters:
    count[letter] = lower.count(letter)

words = len(Lines.split())
print(f'{words} found in the document')

for item in count:
    print(f"The '{item}' character was found {count[item]} times")
