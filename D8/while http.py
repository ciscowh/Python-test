import os
import time
while True:
    time.sleep(1)
    if 'tcp' and '0.0.0.0:80 ' in os.popen('netstat -tulnp').read():
        print('HTTP (TCP/80) 服务已经被打开')
        break
    else:
        print('等待下一秒重新开始')