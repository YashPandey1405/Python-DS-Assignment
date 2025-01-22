# Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of
# keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the
# function should return None

def get_nested_value(nested_dict, keys):
    for key in keys:
        if isinstance(nested_dict, dict) and key in nested_dict:
            nested_dict = nested_dict[key]
        else:
            return None
    return nested_dict

nested_dict = {
    "a": {
        "b": {
            "c": {
                "d": 42
            }
        }
    }
}

keys = ["a", "b", "c", "d"]
result = get_nested_value(nested_dict, keys)
print(result)  

keys = ["a", "b", "x"]
result = get_nested_value(nested_dict, keys)
print(result)  
