# Write a code to check if two given strings are anagrams of each other

word1="listen"
word2="silent"
list=[]

for char in word1:
    list.append(char)

for char in word2:
    if char in list:
        list.remove(char)
    else:
        print("The strings are not anagrams of each other")

if list==[]:
    print("The strings are anagrams of each other")