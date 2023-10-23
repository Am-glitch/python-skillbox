sequence_length = int(input("Введите количество чисел: "))
primes_count = 0

for _ in range(sequence_length):
    number = int(input("Введите число: "))
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        primes_count += 1

print(f"Количество простых чисел в последовательности: {primes_count}.")