# Write a code to reverse a list in-place without using any built-in reverse functions

lst = [1, 2, 2, 3, 4, 4, 4, 5, 5, 1, 3, 2]
n = len(lst)

for i in range((n//2)):
    temp=lst[i]
    lst[i]=lst[n-i-1] 
    lst[n-i-1]=temp

print(lst)
