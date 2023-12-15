def choir_sort(array):
    if len(array) <= 1:
        return array

    base = array[-1]

    left = [x for x in array if x < base]
    right = [x for x in array if x > base]
    middle = [x for x in array if x == base]

    return choir_sort(left) + middle + choir_sort(right)


some_list = [1, 10, 5, 4, 2, 8, 9, 7, 6, 1]

print(choir_sort(some_list))