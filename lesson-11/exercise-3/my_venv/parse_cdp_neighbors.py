# -*- coding: utf-8 -*-
# !/usr/bin/env python3

def parse_cdp_neighbors(command_output):
    my_dict = dict()
    for line in command_output.split('\n'):
        if '>' in line:
            local_dev = line.split('>')[0]
            continue
        else:
            my_list = line.split()
            if len(my_list) > 5 and my_list[3].isdigit():
                remote_dev, local_type, local_num, *other, remote_type, remote_num = my_list
                my_dict[(local_dev, local_type + local_num)] = (remote_dev,remote_type+remote_num)
    return my_dict

if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        print(parse_cdp_neighbors(f.read()))
