import os
import re
ifconfig_result = os.popen('ifconfig').read()
ipv4_add = re.findall('192\.\d{1,3}\.\d{1,3}\.\d\d[^5]',ifconfig_result)[0]
netmask = re.findall('255\.255\.\d{1,3}\.0',ifconfig_result)[0]
boradcast = re.findall('192\.\d\d\d\.\d{1,3}\.255',ifconfig_result)[0]
mac_addr = re.findall('\w+:\w+:\w+:\w+:\w+:\w+',ifconfig_result)[0]

print('{:10}:{:10}' .format('ipv4_add',ipv4_add))
print('{:10}:{:10}' .format('netmask',netmask))
print('{:10}:{:10}' .format('bordcast',boradcast))
print('{:10}:{:10}' .format('mac_addr',mac_addr))
# print(format_string.format())

#产生网关的IP地址
ip_route_result = os.popen('ip route').read()
ipv4_gw = re.match('(\d+\.\d+\.\d+\.)',ipv4_add).group()+re.search('via\s?\d+\.(\d+\.\d+\.(\d+))',ip_route_result).groups()[1]
#打印网关IP地址
print('\n''我们假设网关IP为最后一位，因此网关IP地址为:'+ ipv4_gw +'\n')
#ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()
re_ping_result = re.findall('ttl=\w+',ping_result)

if re_ping_result:
    print('网关可达!')
else:
    print('网关不可达!')
# print(netmask)
# print(boradcast)
# print(mac_addr)
# print(ifconfig_result)
