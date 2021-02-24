import os
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%m-%d %H:%M:%S')
logger = logging.getLogger("test")

print("*"*100)


with open('/data/a.txt', 'w') as f:
    for i in range(100):
        f.write("*"*i+'\n')

time.sleep(10000)
print('success')
