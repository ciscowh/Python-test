import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def qyang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip,True
    else:
        return ip,False
if __name__ == '__main__':
    ping_tong=qyang_ping('192.168.199.77')
    print(ping_tong[1])
    if ping_tong[1]:
        print(f'{ping_tong[0]} 通！')
    else:
        print(f'{ping_tong[0]} 不通!')

from datetime import timezone
timezone(timed)