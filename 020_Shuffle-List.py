# Write a code to shuffle a given list randomly without using any built-in shuffle functions

import random

def shuffle_list(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):  
        j = random.randint(0, i)  
        lst[i], lst[j] = lst[j], lst[i]  

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle_list(lst)
print(lst)
