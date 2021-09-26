lst = [1, 3, 534, 34, 3, 2, 6, 574, 8]
lst1 = []
for i in range(len(lst)):
    for j in range(i, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print (lst)
