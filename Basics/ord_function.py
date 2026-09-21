#The ord() function in Python takes a single character as an argument and returns its Unicode (or ASCII) integer value.

#For example, ord('a') returns 97.

abc = 'Hello I am Rishabh'

print(ord(abc[0]))
print(ord('A'))

# collectively visiting each elements
print([ord(c) for c in 'abc'])