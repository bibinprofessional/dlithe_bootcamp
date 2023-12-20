# LIST

# Lists are used to store multiple items in a single variable
# []
# changeable and allow duplicate values.


# LENGTH 

a=[2,3,4,5,6]
print(len(a))


# ACCESSING ITEMS

print(a[3])

# CHANGE VALUE

a[2]=10
print(a)


# LIST METHODS

# APPEND -> Adds an element at the end of the list

a.append(11)
print(a)

# POP -> Removes the element at the specified position

a.pop(1)
print(a)

# COPY -> Returns a copy of the list

b=a.copy()
print(b)

# INDEX -> Returns the index of the element

print(a.index(10))

# INSERT -> Adds an element at the specified position

a.insert(2,33)
print(a)

# REVERSE -> Reverses the order of the list

a.reverse()
print(a)

# EXTEND -> Add the more elements of a list

b=[1,3,5,6]
a.extend(b)
print(a)

# REMOVE -> Removes the item with the specified value

a.remove(33)
print(a)

# CLEAR -> Removes all the elements from the list

a.clear()
print(a)