#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from D9.paramiko_ssh import qytang_ssh
from D8.test_ping1 import qyang_ping
import re
import pprint

def qytang_get_if(*ips,username='cisco',password='cisco'):
    device_if_dict = {}
    print(device_if_dict)
    for ip in ips:
        if_dict = {}
        if qyang_ping(ip):
            for line in qytang_ssh(ip,username,password,cmd='sh ip int bri').split('\n'):
                print(line)
        device_if_dict[ip] = if_dict

    return device_if_dict

if __name__ == '__main__':
    qytang_get_if('192.168.199.41','192.168.199.43',username='cisco',password='cisco')