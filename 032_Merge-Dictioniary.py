# Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are
# common keys, the values should be added together

dict1 = eval(input("Enter the first dictionary: "))
dict2 = eval(input("Enter the second dictionary: "))
merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
print(merged_dict)
