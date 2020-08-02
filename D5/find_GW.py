import os
import re
from D9.paramiko_ssh import ssh_get_route
from D9.paramiko_ssh import ssh_route
# from D99.paramiko_ssh import ssh_route
# print(ssh_get_route('192.168.199.30','root','pwd@123'))
re_route=ssh_get_route('192.168.199.30','root','pwd@123')
# # # re_route = os.popen('route -n').read()
# # # print(re_route)
re_find_gw = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ssh_route)[1]
# print('网关为：'+re_find_gw)