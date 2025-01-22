# Develop a code that takes a tuple of integers as input. The function should return the maximum and
# minimum values from the tuple using tuple unpacking

def get_max_min(input_tuple):
    max_value = max(input_tuple)
    min_value = min(input_tuple)
    return max_value, min_value

input_tuple = eval(input("Enter a tuple: "))
max_val, min_val = get_max_min(input_tuple)

print("Maximum value:", max_val)
print("Minimum value:", min_val)
