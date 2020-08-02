from D9.paramiko_ssh import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip,username,password):
    try:
        for line in qytang_ssh(ip,username,password,cmd='sh run | begin hostname').split('\n'):
            # m = hashlib.md5()
            # m.update(line.encode())
            # print(m.hexdigest())
    except Exception:
         return
def qytang_check_diff(ip,username='cisco',password='cisco'):
    # before_md5 =
    while True:
        time.sleep(5)
        for line in qytang_ssh(ip,username,password,cmd='sh run | begin hostname').split('\n'):
            m = hashlib.md5()
            m.update(line.encode())
            print(m.hexdigest())
if __name__ == '__main__':
    print(qytang_get_config('192.168.199.41','cisco','cisco'))
    # qytang_check_diff('192.168.199.41','cisco','cisco')