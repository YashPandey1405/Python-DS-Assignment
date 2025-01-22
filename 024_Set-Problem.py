# Develop a code that prompts the user to input two sets of strings. Then, print 
# the elements that are present in the first set but not in the second set

set_input1 = set(input("Enter the elements of the set separated by spaces: ").split())
print("You entered:", set_input1)

set_input2 = set(input("Enter the elements of the set separated by spaces: ").split())
print("You entered:", set_input2)

intersection=set_input1 and set_input2

print("The elements that are present in the first set but not in the second set Is : ",end=" ")
for elem in set_input1:
    if elem not in intersection:
        print(elem,end=" ")

