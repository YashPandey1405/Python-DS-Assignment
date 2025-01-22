# Develop a code that prompts the user to input two sets of strings. 
# Then, print the symmetric difference of these two sets

set_input1 = set(input("Enter the elements of the set separated by spaces: ").split())
print("You entered:", set_input1)

set_input2 = set(input("Enter the elements of the set separated by spaces: ").split())
print("You entered:", set_input2)

ans= set_input1 ^ set_input2
print("The symmetric difference of the two sets is: ", ans)  