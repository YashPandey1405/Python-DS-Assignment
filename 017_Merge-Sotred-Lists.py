#  Write a code to merge two sorted lists into a single sorted list

list1=[1,3,5]
list2=[2,4,6,7]
merged_list = []
i, j = 0, 0

while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

while i < len(list1):
    merged_list.append(list1[i])
    i += 1

while j < len(list2):
    merged_list.append(list2[j])
    j += 1

print(merged_list)