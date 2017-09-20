In [1]: import random

In [2]: values = [1, 2, 3, 4, 5, 6]

In [3]: random.choice(values)
Out[3]: 6

In [4]: random.choice(values)
Out[4]: 4

In [5]: random.choice(values)
Out[5]: 3

In [6]: random.choice(values)
Out[6]: 1

In [7]: random.choice(values)
Out[7]: 1

In [8]: random.sample(values, 2)
Out[8]: [3, 2]

In [9]: random.sample(values, 2)
Out[9]: [6, 2]

In [10]: random.sample(values, 3)
Out[10]: [5, 2, 1]

In [11]: random.sample(values, 3)
Out[11]: [2, 4, 1]

In [12]: random.shuffle(values)

In [13]: values
Out[13]: [3, 2, 1, 6, 5, 4]

In [14]: random.shuffle(values)

In [15]: values
Out[15]: [3, 6, 2, 5, 4, 1]

In [16]: random.randint(0, 10)
Out[16]: 8

In [17]: random.randint(0, 10)
Out[17]: 1

In [18]: random.randint(0, 10)
Out[18]: 9

In [19]: random.randint(0, 10)
Out[19]: 10

In [20]: random.randint(0, 10)
Out[20]: 5

In [21]: random.random()
Out[21]: 0.8589774975043608

In [22]: random.random()
Out[22]: 0.5164782231691775

In [23]: random.random()
Out[23]: 0.033917036851150995

In [24]: random.getrandbits(200)
Out[24]: 139856437077392969591804003765421498586346596645628566012632

In [25]: random.seed()

In [26]: random.getrandbits(200)
Out[26]: 294915326627594158445452397850437153716271745984960033547160

In [27]: random.seed(12345)

In [28]: random.seed(b'bytedata')
