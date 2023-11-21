#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    re_su = []
    for q in range(list_length):
        try:
            re_su.append(my_list_1[q] / my_list_2[q])
        except TypeError:
            print("wrong type")
            re_su.append(0)
        except ZeroDivisionError:
            print("division by 0")
            re_su.append(0)
        except IndexError:
            print("out of range")
            re_su.append(0)
        finally:
            pass
    return re_su
