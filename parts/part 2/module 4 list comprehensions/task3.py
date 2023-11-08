import random

list1 = [random.uniform(5.0, 10.0) for random_num in range(20)]
list2 = [random.uniform(5.0, 10.0) for random_num in range(20)]
winners = [round(list1[competitor], 2) if list1[competitor] > list2[competitor] else round(list2[competitor], 2) for competitor in range(len(list1))]

print(winners)