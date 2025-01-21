# Implement a code to find and remove duplicates from a list while 
# preserving the original order of elements

lst = [1, 2, 2, 3, 4, 4, 4, 5, 5, 1, 3, 2]
seen = set()
i = 0

while i < len(lst):
    if lst[i] in seen:
        lst.pop(i)
    else:
        seen.add(lst[i])
        i += 1

print(lst)


