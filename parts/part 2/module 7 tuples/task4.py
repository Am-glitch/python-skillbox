nums = [number for number in range(0, 10)]
# 0 1 2 3 4 5 6 7 8 9
new_nums = [(nums[i - 1], nums[i]) for i in range(1, len(nums), 2)]

print('Оригинальный список:', nums)
print('Новый список:', new_nums)