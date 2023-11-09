#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        b = my_list
        summ = 0
        u_b = 0
        for k in b:
            mul = k[0] * k[1]
            summ = mul + summ
            u_b = k[1] + u_b
        return summ / u_b
    else:
        return 0
