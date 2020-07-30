import  paramiko
import re
# from D5.find_GW import re_find_gw
def qytang_ssh(ip,username,password,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x= stdout.read().decode()
    return x
def ssh_get_route(ip,username,password,port=22,cmd='route -n'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x= stdout.read().decode()
    return x
if  __name__ == '__main__':
    print(qytang_ssh('192.168.199.30','root','pwd@123'))
    print(qytang_ssh('192.168.199.30','root','pwd@123',cmd='pwd'))
    print('网关为：')
    ssh_route=(ssh_get_route('192.168.199.30','root','pwd@123')

    # A = (ssh_get_route('192.168.199.30','root','pwd@123'))
    # print(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',(ssh_get_route('192.168.199.30','root','pwd@123')))[1])
    # # print(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ssh_get_route('192.168.199.30','root','pwd@123'))[1])