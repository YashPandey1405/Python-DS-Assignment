# Create a code that defines two sets of integers. Then, print the union, 
# intersection, and difference of these two sets

set_input1 = set(input("Enter the elements of the set separated by spaces: ").split())
print("You entered:", set_input1)

set_input2 = set(input("Enter the elements of the set separated by spaces: ").split())
print("You entered:", set_input2)

print(f"Union : {set_input1 or set_input2}")
print(f"Intersection : {set_input1 and set_input2}")
print(f"Difference : {set_input1 - set_input2}")