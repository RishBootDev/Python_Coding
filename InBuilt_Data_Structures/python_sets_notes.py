# ============================================================
# PYTHON SETS — COMPLETE NOTES
# ============================================================
# A set is an unordered collection of UNIQUE elements.
# Sets are mutable, but their elements must be hashable.
# Common uses: removing duplicates, membership checks, and set math.
#
# Note: Set display order is not guaranteed. Examples that depend on
# ordering use sorted(...) to make the output predictable.
# ============================================================


# ------------------------------------------------------------
# 1. CREATING SETS
# ------------------------------------------------------------

# Curly braces create a set when they contain one or more elements.
numbers = {1, 2, 3, 4}
print("1. Set:", numbers)  # Example output: {1, 2, 3, 4} (order may vary)

# set() creates an empty set.
empty_set = set()
print("Empty set:", empty_set)  # set()

# IMPORTANT: {} creates an empty dictionary, not an empty set.
empty_dictionary = {}
print("Type of {}:", type(empty_dictionary).__name__)  # dict

# Duplicate values are automatically removed.
values = {1, 2, 2, 3, 3, 3}
print("Duplicates removed:", sorted(values))  # [1, 2, 3]

# Values can be created from a list, tuple, or string.
from_list = set([1, 2, 2, 3])
from_tuple = set((4, 5, 5, 6))
from_string = set("hello")
print("From list:", sorted(from_list))  # [1, 2, 3]
print("From tuple:", sorted(from_tuple))  # [4, 5, 6]
print("From string:", sorted(from_string))  # ['e', 'h', 'l', 'o']

# A set can contain mixed types if the elements are hashable.
mixed = {1, "python", 3.5, True}
# Note: True and 1 compare equal and have the same hash, so only one remains.
print("Mixed set:", mixed)  # Order may vary; True and 1 represent one element.


# ------------------------------------------------------------
# 2. IMPORTANT SET PROPERTIES
# ------------------------------------------------------------

sample = {10, 20, 30}
print("Number of elements:", len(sample))  # 3
print("Is 20 present?", 20 in sample)  # True
print("Is 99 present?", 99 in sample)  # False

# Sets are unordered: do not rely on indexing or display order.
# sample[0]  # TypeError: 'set' object is not subscriptable

# Set elements must be hashable (usually immutable types).
valid_set = {(1, 2), (3, 4)}  # Tuples of hashable values are allowed.
print("Set of tuples:", valid_set)

# invalid_set = {[1, 2], [3, 4]}  # TypeError: lists are unhashable.
# invalid_set = {{1, 2}, {3, 4}}  # TypeError: sets are unhashable.


# ------------------------------------------------------------
# 3. ADDING ELEMENTS
# ------------------------------------------------------------

fruits = {"apple", "banana"}
fruits.add("orange")
print("After add:", sorted(fruits))  # ['apple', 'banana', 'orange']

# Adding an existing element has no effect.
fruits.add("apple")
print("After adding duplicate:", sorted(fruits))  # Still three elements

# update() adds every element from one or more iterables.
fruits.update(["mango", "grape"])
fruits.update(("pear", "plum"))
print("After update:", sorted(fruits))
# ['apple', 'banana', 'grape', 'mango', 'orange', 'pear', 'plum']

# update() on a string adds its individual characters.
letters = set()
letters.update("cat")
print("Characters added:", sorted(letters))  # ['a', 'c', 't']


# ------------------------------------------------------------
# 4. REMOVING ELEMENTS
# ------------------------------------------------------------

items = {10, 20, 30, 40}

# remove(value) removes the value, but raises KeyError if absent.
items.remove(20)
print("After remove:", sorted(items))  # [10, 30, 40]

# items.remove(99)  # KeyError: 99

# discard(value) removes the value if present; otherwise does nothing.
items.discard(30)
items.discard(99)
print("After discard:", sorted(items))  # [10, 40]

# pop() removes and returns an arbitrary element.
# Because sets are unordered, do not expect a specific popped value.
popped = items.pop()
print("Popped element:", popped)  # Either 10 or 40 in this example
print("Remaining items:", items)

# clear() removes every element.
items.clear()
print("After clear:", items)  # set()


# ------------------------------------------------------------
# 5. LOOPING THROUGH A SET
# ------------------------------------------------------------

colors = {"red", "green", "blue"}

# Loop order is not guaranteed.
print("Loop through colors:")
for color in colors:
    print(color)

# Use sorted() when predictable order is needed.
print("Sorted loop:")
for color in sorted(colors):
    print(color)

# enumerate() gives a counter, but the underlying order is still arbitrary.
for index, color in enumerate(sorted(colors)):
    print(index, color)


# ------------------------------------------------------------
# 6. SET OPERATIONS: UNION
# ------------------------------------------------------------

A = {1, 2, 3}
B = {3, 4, 5}

# Union: elements that are in A OR B.
print("Union using |:", sorted(A | B))  # [1, 2, 3, 4, 5]
print("Union using union():", sorted(A.union(B)))  # [1, 2, 3, 4, 5]

# Union can combine more than two sets.
C = {5, 6}
print("Three-set union:", sorted(A.union(B, C)))  # [1, 2, 3, 4, 5, 6]


# ------------------------------------------------------------
# 7. SET OPERATIONS: INTERSECTION
# ------------------------------------------------------------

# Intersection: elements present in BOTH sets.
print("Intersection using &:", sorted(A & B))  # [3]
print("Intersection using intersection():", sorted(A.intersection(B)))  # [3]

# Find common elements across three sets.
C = {3, 5, 6}
print("Three-set intersection:", sorted(A & B & C))  # [3]


# ------------------------------------------------------------
# 8. SET OPERATIONS: DIFFERENCE
# ------------------------------------------------------------

# A - B: elements in A that are NOT in B.
print("A - B:", sorted(A - B))  # [1, 2]
print("B - A:", sorted(B - A))  # [4, 5]

# Difference is directional: A - B may differ from B - A.
print("A.difference(B):", sorted(A.difference(B)))  # [1, 2]


# ------------------------------------------------------------
# 9. SET OPERATIONS: SYMMETRIC DIFFERENCE
# ------------------------------------------------------------

# Symmetric difference: elements in either set, but NOT in both.
print("Symmetric difference using ^:", sorted(A ^ B))  # [1, 2, 4, 5]
print("Using symmetric_difference():", sorted(A.symmetric_difference(B)))
# [1, 2, 4, 5]


# ------------------------------------------------------------
# 10. SET COMPARISONS
# ------------------------------------------------------------

small = {1, 2}
large = {1, 2, 3}
same = {2, 1}

print("Equal sets:", small == same)  # True (order does not matter)
print("Not equal:", small != large)  # True

# Subset: every element of small is in large.
print("small <= large:", small <= large)  # True
print("small.issubset(large):", small.issubset(large))  # True
print("small < large:", small < large)  # True: proper subset

# Superset: every element of small is in large_set.
print("large >= small:", large >= small)  # True
print("large.issuperset(small):", large.issuperset(small))  # True
print("large > small:", large > small)  # True: proper superset

# A set is a subset of itself, but not a proper subset of itself.
print("small <= same:", small <= same)  # True
print("small < same:", small < same)  # False

# Disjoint sets have no common elements.
X = {1, 2}
Y = {3, 4}
Z = {2, 3}
print("X and Y disjoint:", X.isdisjoint(Y))  # True
print("X and Z disjoint:", X.isdisjoint(Z))  # False


# ------------------------------------------------------------
# 11. IN-PLACE SET OPERATIONS
# ------------------------------------------------------------

# These operations modify the original set.
left = {1, 2, 3}
left.update({3, 4})  # In-place union
print("update:", sorted(left))  # [1, 2, 3, 4]

left = {1, 2, 3}
left.intersection_update({2, 3, 4})
print("intersection_update:", sorted(left))  # [2, 3]

left = {1, 2, 3}
left.difference_update({2})
print("difference_update:", sorted(left))  # [1, 3]

left = {1, 2, 3}
left.symmetric_difference_update({3, 4})
print("symmetric_difference_update:", sorted(left))  # [1, 2, 4]


# ------------------------------------------------------------
# 12. SET COMPREHENSIONS
# ------------------------------------------------------------

# Syntax: {expression for item in iterable if condition}

squares = {n * n for n in range(1, 6)}
print("Squares:", sorted(squares))  # [1, 4, 9, 16, 25]

even_squares = {n * n for n in range(1, 11) if n % 2 == 0}
print("Squares of even numbers:", sorted(even_squares))
# [4, 16, 36, 64, 100]

# Duplicate results are automatically removed.
remainders = {n % 3 for n in range(10)}
print("Remainders:", sorted(remainders))  # [0, 1, 2]

# Convert words to lowercase unique first letters.
words = ["Apple", "ant", "Banana", "boat"]
first_letters = {word[0].lower() for word in words}
print("First letters:", sorted(first_letters))  # ['a', 'b']


# ------------------------------------------------------------
# 13. REMOVING DUPLICATES FROM A LIST
# ------------------------------------------------------------

numbers = [4, 2, 4, 1, 2, 5, 1]
unique_set = set(numbers)
print("Unique values:", sorted(unique_set))  # [1, 2, 4, 5]

# Converting directly to list does NOT preserve the original order.
unique_list_unordered = list(set(numbers))
print("Unique list (order not guaranteed):", unique_list_unordered)

# To preserve the first occurrence order, use dict.fromkeys().
unique_preserving_order = list(dict.fromkeys(numbers))
print("Unique list (original order):", unique_preserving_order)
# [4, 2, 1, 5]


# ------------------------------------------------------------
# 14. COMMON PRACTICAL PATTERNS
# ------------------------------------------------------------

# A. Check whether a list contains duplicates.
def contains_duplicates(values):
    return len(values) != len(set(values))

print("Has duplicates [1, 2, 3]:", contains_duplicates([1, 2, 3]))
# False
print("Has duplicates [1, 2, 1]:", contains_duplicates([1, 2, 1]))
# True

# B. Find common values between two lists.
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
common = set(list_a) & set(list_b)
print("Common values:", sorted(common))  # [3, 4]

# C. Find values that appear in the first list but not the second.
only_a = set(list_a) - set(list_b)
print("Only in first list:", sorted(only_a))  # [1, 2]

# D. Check whether two lists have any common values.
has_common = not set(list_a).isdisjoint(list_b)
print("Lists have common values:", has_common)  # True

# E. Find missing numbers from a range.
present = {1, 2, 4, 6}
expected = set(range(1, 7))
missing = expected - present
print("Missing numbers:", sorted(missing))  # [3, 5]

# F. Find unique vowels in a string.
text = "programming in python"
vowels = set("aeiou")
found_vowels = set(text.lower()) & vowels
print("Vowels found:", sorted(found_vowels))  # ['a', 'i', 'o']


# ------------------------------------------------------------
# 15. SET VS LIST VS TUPLE
# ------------------------------------------------------------

# list: ordered, mutable, duplicates allowed, indexable.
# tuple: ordered, immutable, duplicates allowed, indexable.
# set: unordered, mutable, duplicates removed, not indexable.

list_example = [1, 2, 2, 3]
tuple_example = (1, 2, 2, 3)
set_example = {1, 2, 2, 3}

print("List:", list_example)    # [1, 2, 2, 3]
print("Tuple:", tuple_example)  # (1, 2, 2, 3)
print("Set:", sorted(set_example))  # [1, 2, 3]


# ------------------------------------------------------------
# 16. FROZENSET
# ------------------------------------------------------------

# frozenset is an immutable version of a set.
frozen = frozenset([1, 2, 2, 3])
print("Frozenset:", frozen)  # frozenset({1, 2, 3}) (display order may vary)

# frozen.add(4)  # AttributeError: frozenset has no add() method

# Because a frozenset is immutable and hashable, it can be an element of a set.
set_of_frozensets = {frozenset({1, 2}), frozenset({3, 4})}
print("Set of frozensets:", set_of_frozensets)


# ------------------------------------------------------------
# 17. IMPORTANT PITFALLS
# ------------------------------------------------------------

# 1. Empty set:
print("Empty set:", set())  # set()
print("Empty dictionary:", {})  # {}

# 2. Duplicate values disappear:
print("Duplicates:", {1, 1, 1, 2})  # {1, 2} (order may vary)

# 3. Sets do not support indexing:
# values = {10, 20, 30}
# print(values[0])  # TypeError

# 4. Mutable values such as lists and dictionaries cannot be set elements:
# bad = {[1, 2], [3, 4]}  # TypeError

# 5. remove() raises KeyError if the element is missing; discard() does not.
example = {1, 2}
example.discard(99)  # Safe; no error.
print("discard missing item:", sorted(example))  # [1, 2]

# 6. Do not assume set iteration order.
# Use sorted(my_set) when you need a predictable order and elements are comparable.

# 7. 1, True, and 1.0 compare equal, so they count as one set element.
bool_number_set = {1, True, 1.0}
print("1, True, 1.0 count:", len(bool_number_set))  # 1


# ------------------------------------------------------------
# 18. TIME COMPLEXITY (AVERAGE CASE)
# ------------------------------------------------------------

# Operation                         Typical average time
# -------------------------------------------------------
# len(my_set)                       O(1)
# value in my_set                   O(1)
# add(value)                        O(1)
# remove(value) / discard(value)    O(1)
# union                             O(len(A) + len(B))
# intersection                      Usually proportional to smaller/larger set
# difference                        Depends on the set sizes and implementation
# Sorting a set                     O(n log n)
#
# Membership/add/remove are average O(1), not guaranteed O(1) in every case.
# Hash collisions and pathological inputs can affect performance.