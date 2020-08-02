import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def qyang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip,True

    # else:
    #     return ip,False
if __name__ == '__main__':
    ping_tong = qyang_ping('192.168.199.1')
    if ping_tong[1]:
        print(f'{ping_tong[0]} 通！')
    else:
        print(f'{ping_tong[0]} 不通!')
# class Person:
#     def __init__(self, name, age, pay=0, job=None):
#         self.name = name
#         self.age = age
#         self.pay = pay
#         self.job = job
#     def getlastname(self):
#         return self.name.split()[-1]
#     def getbouns(self,percent):
#         self.pay = int(self.pay * (1.1 + percent))
# if __name__ == '__main__':
#     tony = Person('wang hui',33,5000,'sales')
#     print(tony.age)
#     # tony.pay *=1.1
#     # print(int(tony.pay))
#     print(tony.job)
#     print(tony.getlastname())
#     tony.getbouns(0.1)
#     print(tony.pay)