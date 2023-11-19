def c_zip(iterable1, iterable2):
    min_iterable = min(iterable1, iterable2, key=len)
    for index, _ in enumerate(min_iterable):
        yield iterable1[index], iterable2[index]

string = 'abcde'
arr = [1, 2, 3, 4, 5]
num_tpl = (10, 20, 30, 40, 50)

generated_result = c_zip(arr, num_tpl)

for tpl in generated_result:
    print(tpl)
