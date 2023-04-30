def unique_element(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(unique_element([1, 1, 2, 3, 3, 4, 5, 5, 5]))
