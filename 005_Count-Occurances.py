# Write a code to find all occurrences of a given substring within another string

def count_occurances(string, substring):
    occurrences = []
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        occurrences.append(start)
        start += 1
    return occurrences

string = "This is a test string for testing substring test"
substring = "test"
result = count_occurances(string, substring)
print(result)
