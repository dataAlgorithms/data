In [118]: import numpy as np

In [119]: m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])

In [120]: m
Out[120]:
matrix([[ 1, -2,  3],
        [ 0,  4,  5],
        [ 7,  8, -9]])

In [121]: m.T
Out[121]:
matrix([[ 1,  0,  7],
        [-2,  4,  8],
        [ 3,  5, -9]])

In [122]: m
Out[122]:
matrix([[ 1, -2,  3],
        [ 0,  4,  5],
        [ 7,  8, -9]])

In [123]: m.I
Out[123]:
matrix([[ 0.33043478, -0.02608696,  0.09565217],
        [-0.15217391,  0.13043478,  0.02173913],
        [ 0.12173913,  0.09565217, -0.0173913 ]])

In [124]: v = np.matrix([[2], [3], [4]])

In [125]: v
Out[125]:
matrix([[2],
        [3],
        [4]])

In [126]: m * v
Out[126]:
matrix([[ 8],
        [32],
        [ 2]])

In [127]: import numpy.linalg

In [128]: numpy.linalg.det(m)
Out[128]: -229.99999999999983

In [129]: numpy.linalg.eigvals(m)
Out[129]: array([-13.11474312,   2.75956154,   6.35518158])

In [130]: x = numpy.linalg.solve(m, v)

In [131]: x
Out[131]:
matrix([[ 0.96521739],
        [ 0.17391304],
        [ 0.46086957]])

In [132]: m * x
Out[132]:
matrix([[ 2.],
        [ 3.],
        [ 4.]])

In [133]: v
Out[133]:
matrix([[2],
        [3],
        [4]])
