import tqdm
import numpy as np

a = []
i = 0
while True:
    a.append(np.random.rand(1000))
    if i % 10000 == 0:
        print(i)
    i += 1
