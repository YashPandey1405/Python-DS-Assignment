# Create a code that takes a tuple and two integers as input. The function should return a new tuple
# containing elements from the original tuple within the specified range of indices

tuple_input1 = eval(input("Enter a tuple: "))
print("You entered:", tuple_input1)
ans=[]
print()

start=int(input("Enter The Start Range : "))
end=int(input("Enter The End Range : "))
for elem in tuple_input1:
    if elem>=start and elem<=end:
        ans.append(elem)

ans=tuple(ans)
print("Tuple after applying the range:", ans)