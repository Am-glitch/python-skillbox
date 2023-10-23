N = int(input())
max_sum = 0
max_number = 0

for i in range(N):
    number = int(input())
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
        max_sum = max(digit_sum, max_sum)
        if max_sum == max(digit_sum, max_sum):
            max_number = number

print(max_sum, number)