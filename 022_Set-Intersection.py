# Create a code that prompts the user to enter two sets of integers separated by commas. 
# Then, print the intersection of these two sets

set_input1 = set(input("Enter the elements of the set separated by spaces: ").split())
print("You entered:", set_input1)

set_input2 = set(input("Enter the elements of the set separated by spaces: ").split())
print("You entered:", set_input2)

print(f"The Intersection Is : {set_input1 and set_input2}")
