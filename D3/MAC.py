import re
MAC = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
re_result = re.match('(\d\d\d)\s(\d\d\w\d.\d\d\w\d.\d\d\d\d)\s(\w+)\s(\w\w\d\/\d\/\d\d)',MAC).groups()
vlanid = re_result[0]
mac  = re_result[1]
type = re_result[2]
interface= re_result[3]
str_vlan = 'VLAN ID'
str_mac  = 'MAC'
str_type = 'TYPE'
str_interface = 'Interface'
line1 = f'{str_vlan:<10}:{vlanid:<10}'
line2 = f'{str_mac:<10}:{mac:<10}'
line3 = f'{str_type:<10}:{type:<10}'
line4 = f'{str_interface:<10}:{interface:<10}'
print(line1)
print(line2)
print(line3)
print(line4)