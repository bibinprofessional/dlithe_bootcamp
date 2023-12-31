# find the element 12 in the list and change to 13

l=[1,14,13,5,12,55,32,6,7]
for i in range(len(l)):
    if l[i]==12:
        l[i]=13

print(l)
print()

# find the element 12 and remove

l2=[1,14,13,5,12,55,32,6,7]
l2.remove(12)
print(l2)
print()

# remove all elements from the list one by one and print the resultant list simultaneously

l3=[1,14,13,5,12,55,32,6,7]
for i in range(len(l3)):
    l.pop()
    print(l)

print()

# merge 2 list

l4=[1,14,13,5,12]
l5=[5,34,325,2]

l4.extend(l5)
print(l4)
print()

# clear all elements from the list

l6=[1,14,13,5,12,55,32,6,7]

l6.clear()
print(l6)
print()

# find modulus 5 of all elements in the list

l7=[1,14,13,5,12,55,32,6,7]

for i in range(len(l7)):
    l7[i]=l7[i]%5

print(l7)

# create a list list comprehension 
l8=[i for i in range(10)]
print(l8)


# create a list of squared list using list comprehension
l9=[i*i for i in l8]
print(l9)


# create a list with only even number
l10=[i for i in l8 if i%2==0]
print(l10)

# even and odd
l11=['even' if i%2==0 else 'odd' for i in l8]
print(l11)