import re
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
port = re.match('^eth 1/101/(\d+)/(\d+)',port_list[0]).groups(),re.match('^eth 1/101/(\d+)/(\d+)',port_list[1]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[2]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[3]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[4]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[5]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[6]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[7]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[8]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[9]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)',port_list[10]).groups(),\
       re.match('^eth 1/101/(\d+)/(\d+)', port_list[11]).groups(),
a = sorted(port,key=lambda x: (x[0],x[1]))
print(['{:1}/{:1}/{:1}' .format('eth1/10',a[0][0],a[0][1]),'{:1}/{:1}/{:1}' .format('eth1/10',a[1][0],a[1][1]),'{:1}/{:1}/{:1}' .format('eth1/10',a[2][0],a[2][1]),
       '{:1}/{:1}/{:1}' .format('eth1/10',a[3][0],a[3][1]),'{:1}/{:1}/{:1}' .format('eth1/10',a[4][0],a[4][1]),
       '{:1}/{:1}/{:1}' .format('eth1/10',a[5][0],a[5][1]),'{:1}/{:1}/{:1}' .format('eth1/10',a[6][0],a[6][1]),
       '{:1}/{:1}/{:1}' .format('eth1/10',a[7][0],a[7][1]),'{:1}/{:1}/{:1}' .format('eth1/10',a[8][0],a[8][1]),
       '{:1}/{:1}/{:1}' .format('eth1/10',a[9][0],a[9][1]),'{:1}/{:1}/{:1}' .format('eth1/10',a[10][0],a[10][1]),])