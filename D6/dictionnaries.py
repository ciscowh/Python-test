import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n \
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
s_d_ip_1 = re.findall('\d+\.\d+\.\d+\.\d+',asa_conn)[0],re.findall(':(\d+)',asa_conn)[0],re.findall('\d+\.\d+\.\d+\.\d+',asa_conn)[1],re.findall(':(\d+)',asa_conn)[1]
s_d_ip_2 = re.findall('\d+\.\d+\.\d+\.\d+',asa_conn)[2],re.findall(':(\d+)',asa_conn)[4],re.findall('\d+\.\d+\.\d+\.\d+',asa_conn)[3],re.findall(':(\d+)',asa_conn)[5]
bytes_1 = re.findall('bytes (\d+)',asa_conn)[0],re.findall('flags (\w+)',asa_conn)[0]
bytes_2 = re.findall('bytes (\d+)',asa_conn)[1],re.findall('flags (\w+)',asa_conn)[1]
asa_dict =  {s_d_ip_1:bytes_1,s_d_ip_2:bytes_2}
print('打印分析后的字典：\n')
print(asa_dict)

src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags  = 'flags'
print('\n格式化打印输出\n')
for k,v in asa_dict.items():
    print(f'{src:^8}:{k[0]:^8}|{src_ip:^8}:{k[1]:^8}| {dst:^8}:{k[2]:^8}:{dst_ip:^8}:{k[3]:^8}')
    print(f'{bytes_name:^8}:{v[0]:^8}|{flags:^8}:{v[1]:^8}')
    print('='*80)