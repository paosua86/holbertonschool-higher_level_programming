#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            list = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            list = 0
        except (ValueError, TypeError):
            print("wrong type")
            list = 0
        except (IndexError):
            print("out of range")
            list = 0
        finally:
            new_list.append(list)
    return (new_list)
