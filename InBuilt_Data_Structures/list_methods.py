# adding elements in a list

list = [1, 2, 3, 5, 6, 7]
list.append(9)       # add an element to the end

# insert element at a particular index
list.insert(2, 55)

#removing element
list.remove(55) ## it removes the first occurence of the element

# to remove the last occurence of the number we need to remove
list.append(55)
list.append(55)
list.pop(55)

# to count the frequency of an element
list.count(55)

# to sort this list
list.sort()

# to reverse the list
list.reverse()

# to clear this list
list.clear()
