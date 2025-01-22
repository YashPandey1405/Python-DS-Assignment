# Write a code that takes two tuples as input and returns a 
# new tuple containing elements that are common to both input tuples

tuple_input1 = eval(input("Enter a tuple: "))
print("You entered:", tuple_input1)

tuple_input2 = eval(input("Enter a tuple: "))
print("You entered:", tuple_input2)

ans_tuple = tuple(set(tuple_input1) & set(tuple_input2))
print("The intersection of the two tuples is:", ans_tuple)