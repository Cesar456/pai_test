from hdfsutils import hive
import os
import torch
import tensorflow as tf

from tensorflow.python.client import device_lib


data = hive.get_table_full_data('tmp', 'tmp_account_risk_steal_result_0308', partition_dict={1:1, "2":2}, row_format=',')

print(len(data))
print(data[:10])

print(torch.cuda.is_available())
print(torch.cuda.get_device_name())
print(torch.cuda.device_count())

gpu_device_name = tf.test.gpu_device_name()
print(gpu_device_name)
print(tf.test.is_gpu_available())

