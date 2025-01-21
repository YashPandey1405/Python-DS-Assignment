# Write a code to determine if a string has all unique characters

def has_unique_characters(s):
    return len(s) == len(set(s))

string = "abcdefg"
result = has_unique_characters(string)
print(result) 

string = "aabbcc"
result = has_unique_characters(string)
print(result)  
