#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for element in range(len(new_list)):
        if (my_list[element] % 2) == 0:
            new_list[element] = True
        else:
            new_list[element] = False
    return (new_list)
