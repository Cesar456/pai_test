import os
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%m-%d %H:%M:%S')
logger = logging.getLogger("test")


print(os.path.abspath('/mnt/nfs-storage'))
logger.info('test')
time.sleep(100)
