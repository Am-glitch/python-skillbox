def tpl_sort(tpl):
    if (all(isinstance(num, int) for num in tpl)):
        return tuple(sorted(tpl))
    return tpl

tpl = (6, 3, -1, 8, 4, 10, -5)

print(tpl_sort(tpl))