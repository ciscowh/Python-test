#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from D9.paramiko_ssh import qytang_ssh
from D8.test_ping1 import qyang_ping
import re
import pprint

def qytang_get_if(*ips,username='cisco',password='cisco'):
    device_if_dict = {}
    for ip in ips:
        if_dict = {}
        if qyang_ping(ip):
            for line in qytang_ssh(ip,username,password,cmd='sh ip int bri').split('\n\r'):
                #print(line)
                re_result = re.findall('([A-Z]\S+\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line)
                if re_result:
                    if_dict[re_result[0][0]] = re_result[0][1]
                    if_dict[re_result[1][0]] = re_result[1][1]
                    if_dict[re_result[2][0]] = re_result[2][1]
                    if_dict[re_result[3][0]] = re_result[3][1]
        device_if_dict[ip] = if_dict
    return device_if_dict
if __name__ == '__main__':
    pprint.pprint(qytang_get_if('192.168.199.41','192.168.199.43',username='cisco',password='cisco'),indent=4)