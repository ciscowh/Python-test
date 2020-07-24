import os
import re
re_route = os.popen('route -n').read()
print(re_route)

re_find_gw = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',re_route)[1]
print('网关为：'+re_find_gw)