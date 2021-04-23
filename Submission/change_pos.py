def change_pos(lis):
    for i in range(0, len(lis), 3):
        lis[i], lis[i + 1] = lis[i + 1], lis[i]

    return lis


lis = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(change_pos(my_list))