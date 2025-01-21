# Write a code to count the number of vowels in a string

name="YashPandey"
vowels = 'aeiouAEIOU'
count = 0

for char in name:
    if char in vowels:
        count += 1

print(count)