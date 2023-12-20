input_string = input("Enter a sentence: ")

# Splitting the input sentence into words
words = input_string.split()

# Creating an empty dictionary to store word counts
word_count = {}

# Counting the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Dictionary:", word_count)