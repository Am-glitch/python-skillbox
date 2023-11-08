def merge_sorted_lists(arr1, arr2):
    return sorted(set(arr1 + arr2))

list1 = [10, 8 , 6]
list2 = [2]
merged = merge_sorted_lists(list1, list2)
print(merged)