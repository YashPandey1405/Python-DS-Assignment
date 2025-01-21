# Create a code to check if a given list is sorted (either in ascending or descending order) or not

def Ascending_Order(lst):
    return lst == sorted(lst)

lst=[1,2,3,4,5,6,7,8,9]
# lst = [9, 8, 7]

check_Ascending_Order = Ascending_Order(lst)
if check_Ascending_Order:
    print("The list is in ascending order")
else:
    check_Descending_Order = Ascending_Order(lst[::-1])  
    if check_Descending_Order:
        print("The list is in descending order")
    else:
        print("The list is not sorted")
