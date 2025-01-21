# Implement a code to find the second largest number in a given list of integers

list = [1, 2, 3, 4, 1, 2, 4, 2, 4, 2, 2, 1, 5, 6, 10, 7, 8]

largest = float('-inf')  
second = float('-inf')  

for elem in list:
    if elem > largest:
        second = largest
        largest = elem
    elif elem > second and elem != largest:
        second = elem

print(second)
