# Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You
# can choose whether to sort in ascending or descending order

def sort_dict_by_values(input_dict, ascending=True):
    return dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=not ascending))

data = {"apple": 5, "banana": 2, "cherry": 8, "date": 3}

sorted_asc = sort_dict_by_values(data, ascending=True)
print("Ascending:", sorted_asc)

sorted_desc = sort_dict_by_values(data, ascending=False)
print("Descending:", sorted_desc)
