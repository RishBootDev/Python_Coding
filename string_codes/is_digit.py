# 1. Digits Only
number_string = "12345"
print(number_string.isdigit())  # Output: True

# 2. Mixed Characters
mixed_string = "12345abc"
print(mixed_string.isdigit())  # Output: False

# 3. Empty String
empty_string = ""
print(empty_string.isdigit())   # Output: False

# 4. Spaces Included
spaced_string = " 12345 "
print(spaced_string.isdigit())  # Output: False