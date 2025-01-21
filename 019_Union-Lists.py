# Create a code to find the union of two lists without duplicates

list1=[1,2,3,4,5,6,7]
list2=[2,4,5,6,7,8,9]
ans=set()

for elem in list1:
    ans.add(elem)

for elem in list2:
    ans.add(elem)

print(ans)