result = []
for number in range(15, 101):
    if (int(str(number)[0]) * int(str(number)[1]) * 3) == number: result.append(number)

print(result)