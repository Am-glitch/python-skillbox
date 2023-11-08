def max_people_for_rollerblades(rollers, feet):
    rollers.sort(reverse=True)  
    feet.sort(reverse=True)

    max_people = 0

    i_roller = 0
    j_foot = 0

    while i_roller < len(roller_sizes) and j_foot < len(foot_sizes):
        if foot_sizes[j_foot] == roller_sizes[i_roller]:
            max_people += 1
            i_roller += 1
            j_foot += 1
        else:
            j_foot += 1

    return max_people

num_rollers = int(input("Количество роликов: "))
roller_sizes = [int(input(f"Размер пары {i + 1}: ")) for i in range(num_rollers)]

num_people = int(input("Количество людей: "))
foot_sizes = [int(input(f"Размер ноги человека {i + 1}: ")) for i in range(num_people)]

result = max_people_for_rollerblades(roller_sizes, foot_sizes)
print(f"Наибольшее количество людей, которые могут взять ролики: {result}")
