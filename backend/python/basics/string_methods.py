# STRING METHODS

# CAPITALIZE ->	Converts the first character to upper case

a='stringfdsfsdtwerwds'
a=a.capitalize()
print(a)

# COUNT -> Returns the number of times a specified value occurs in a string

# print(a.count('d'))

# ISALNUM -> Returns True if all characters in the string are alphanumeric

print(a.isalnum())

# ISALPHA -> Returns True if all characters in the string are in the alphabet

print(a.isalpha())

# ISNUMERIC -> Returns True if all characters in the string are numeric
b='1234'
print(b.isnumeric())

# ISLOWER -> Returns True if all characters in the string are lower case
a='stringfdsTsdtwerwds'
print(a.islower())

# LOWER -> 	Converts a string into lower case

print(a.lower())

# ISUPPER -> Returns True if all characters in the string are upper case
c='ADAS'
print(c.isupper())

# UPPER -> Converts a string into upper case

print(a.upper())

# STRIP -> cut ending and beginning

a='dafsds a sfada'
print(a.rstrip('da'))

# SPLIT -> 	Splits the string at the specified separator, and returns a list

c='das asd fdas fds'
print(c.split('a'))

# REPLACE -> Returns a string where a specified value is replaced with a specified value

print(c.replace('d','k'))

# SWAPCASE -> Swaps cases, lower case becomes upper case and vice versa

d='asdsaTRYTSH'
print(d.swapcase())
