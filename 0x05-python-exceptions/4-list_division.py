#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx = 0
    result = []
    if list_length < idx:
        print("out of range")
    while idx < list_length:
        try:
            result.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            idx += 1
    return result
