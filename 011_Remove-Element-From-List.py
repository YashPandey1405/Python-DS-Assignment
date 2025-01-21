# Write a code to remove all occurrences of a specific element from a list

list=[1,2,3,4,1,2,4,2,4,2,2,1,5,6]
element=2

while(element in list):
    list.remove(element)

print(list)