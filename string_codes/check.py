# 1. Only Letters
text1 = "HelloWorld"
print(text1.isalpha())  # Output: True

# 2. Contains a Space
text2 = "Hello World"
print(text2.isalpha())  # Output: False

# 3. Contains Digits
text3 = "Hello123"
print(text3.isalpha())  # Output: False

# 4. Special Characters
text4 = "Hello@World"
print(text4.isalpha())  # Output: False

# 5. Empty String
text5 = ""
print(text5.isalpha())  # Output: False