# Write a code that takes a list of words as input and returns a dictionary where the keys are unique words
# and the values are the frequencies of those words in the input list

words = input("Enter a list of words separated by spaces: ").split()
word_freq = {word: words.count(word) for word in set(words)}
print(word_freq)
