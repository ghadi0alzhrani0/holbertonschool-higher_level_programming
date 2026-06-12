#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_first = 0
    a_second = 0
    b_first = 0
    b_second = 0

    if len(tuple_a) > 0:
        a_first = tuple_a[0]
    if len(tuple_a) > 1:
        a_second = tuple_a[1]

    if len(tuple_b) > 0:
        b_first = tuple_b[0]
    if len(tuple_b) > 1:
        b_second = tuple_b[1]

    return (a_first + b_first, a_second + b_second)
