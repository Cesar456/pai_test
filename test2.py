import os
import sys
import logging
import time
from hdfsutils import hdfs


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%m-%d %H:%M:%S')
logger = logging.getLogger("test")

print("*"*100)

print(sys.argv)

with open('/common/a.txt', 'w') as f:
    for i in range(100):
        f.write("*"*i+'\n')

time.sleep(1000)
print('success')

hdfs.get('/tmp/cesar//ttt.txt', '/data/ahdfs.txt')
