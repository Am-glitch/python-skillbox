num = int(input('введите четырехзначное число: '))

fourthNum = num % 10
thirdNum = num % 100 - fourthNum
secondNum = num % 1000 - thirdNum - fourthNum
firstNum = num % 10000 - secondNum - thirdNum - fourthNum

print(f'{firstNum} {secondNum} {thirdNum} {fourthNum}')