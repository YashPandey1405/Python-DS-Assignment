# Write a code that takes a tuple and an element as input. The function should return the count of
# occurrences of the given element in the tuple

tuple_input1 = eval(input("Enter a tuple: "))
element = input("Enter an target element: ")
count=0

for elem in tuple_input1:
    if elem == element:
        count += 1
print(f"The Element {element} Occured {count} Times")