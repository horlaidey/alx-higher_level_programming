#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            my_str = my_string[:i] + my_string[i+1:]
            return no_c(my_str)
