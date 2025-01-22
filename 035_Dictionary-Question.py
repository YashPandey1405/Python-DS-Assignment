# Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary
# correctly handles cases where multiple keys have the same value by storing the keys as a list in the
# inverted dictionary.

def invert_dictionary(input_dict):
    inverted = {}
    for key, value in input_dict.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted

data = {"a": 1, "b": 2, "c": 1, "d": 3}

result = invert_dictionary(data)
print(result)  