import  paramiko
import re
def qytang_ssh(ip,username,password,port=22,cmd='sh run | begin hostname'):
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
    ssh_route = ssh_get_route('192.168.199.30', 'root', 'pwd@123')
    # from D5.find_GW import re_find_gw
    print(qytang_ssh('192.168.199.41','cisco','cisco'))
    print(qytang_ssh('192.168.199.42','cisco','cisco',))
    # print('网关为：')
    # print(re_find_gw)