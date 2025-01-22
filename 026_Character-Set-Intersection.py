# Write a code that prompts the user to input two sets of characters. 
# Then, print the union of these two sets

# Input two sets
set_input1 = set(input("Enter the elements of the first set separated by spaces: ").split())
print("You entered:", set_input1)

set_input2 = set(input("Enter the elements of the second set separated by spaces: ").split())
print("You entered:", set_input2)

# Perform the set intersection using the & operator
intersection = set_input1 & set_input2
print("Intersection of the two sets:", intersection)
