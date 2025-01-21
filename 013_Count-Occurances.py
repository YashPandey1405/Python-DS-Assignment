# Create a code to count the occurrences of each element in a list and 
# return a dictionary with elements as keys and their counts as values

from collections import Counter

lst = [1, 2, 2, 3, 4, 4, 4, 5, 5, 1, 3, 2]
result = dict(Counter(lst))
print(result)
