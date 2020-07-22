import re
str1='Port-channel1.189   192.168.189.254 YES CONFIG up'
re_result = re.match('(\w+.\w+\d.\d\d\d)\s*(\d\d\d.\d\d\d.\d\d\d.\d\d\d)\s?\w+\s?\w+\s?(\w+)',str1).groups()
port = re_result[0]
IP = re_result[1]
status = re_result[2]
str_po = '接口'
str_ip = 'IP地址'
str_status = '状态'
line1 = f'{str_po:<6}:{port:<10}'
line2 = f'{str_ip:<6}:{IP:<10}'
line3 = f'{str_status:<6}:{status:<10}'
print('-'*80)
print(line1)
print(line2)
print(line3)

# line1='{:8}:{}' .format('接口',str_port)
# line2='{:8}:{}' .format('IP地址',str_ip)
# line3='{:8}:{}' .format('状态',str_status)
#
#
# print('-'*100)
# print(line1)
# print(line2)
# print(line3)