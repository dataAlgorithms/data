#! coding=utf-8

'''
:::vector_add
[150, 330, 70]

:::vector_sub
[-10, 10, 10]

:::vectorsum
[150, 330, 70]

:::vectorsum_reduce
[150, 330, 70]

:::vectorsum_partial
[150, 330, 70]

:::scalar_multiply
[700, 1700, 400]

:::scalar_mean
[75.0, 165.0, 35.0]

:::dot
34000

:::sum_of_squares
35400

:::distance
17.3205080757

:::shape
(2, 3)
(3, 2)

:::get_row and get_column
[1, 2, 3]
[2, 5]

:::friends_of_five
[4, 6, 7]

'''
height_weight_age = [70, # inches,
                     170,# pounds,
                     40] # year

height_weight_age1 = [80,
                      160,
                      30]

grades = [95, # exam1
          80, # exam2
          75, # exam3
          62] # exam4

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

print ':::vector_add'
print vector_add(height_weight_age, height_weight_age1)

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

print '\r:::vector_sub'
print vector_subtract(height_weight_age, height_weight_age1)

def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

print '\r:::vectorsum'
print vector_sum([height_weight_age, height_weight_age1])

def vector_sum_reduce(vectors):
    return reduce(vector_add, vectors)

print '\r:::vectorsum_reduce'
print vector_sum_reduce([height_weight_age, height_weight_age1])

from functools import partial
vector_sum_partial = partial(reduce, vector_add)

print '\r:::vectorsum_partial'
print vector_sum_partial([height_weight_age, height_weight_age1])

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

print '\r:::scalar_multiply'
print scalar_multiply(10, height_weight_age)

def vector_mean(vectors):
    """Compute the vector whose ith elements is the mean of
    the ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1.0/n, vector_sum(vectors))

print '\r:::scalar_mean'
print vector_mean([height_weight_age, height_weight_age1])

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

print '\r:::dot'
print dot(height_weight_age, height_weight_age1)

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

print '\r:::sum_of_squares'
print sum_of_squares(height_weight_age)

import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v_1-w_1) ** 2 + ... + (v_n_w_n)**2"""
    return sum_of_squares(vector_subtract(v,w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

def distance_new(v, w):
    return magnitude(vector_subtract(v, w))

print '\r:::distance'
print distance(height_weight_age, height_weight_age1)

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

print '\r:::shape'
print shape(A)
print shape(B)

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j]
            for A_i in A]

print '\r:::get_row and get_column'
print get_row(A, 0)
print get_column(A, 1)

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i, j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]

def is_diagonal(i, j):
    """1's on the diagonal
       0's everywhere else"""
    return 1 if i == j else 0

ientify_matrix = make_matrix(5, 5, is_diagonal)

friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9

friends_of_five = [i
                  for i, is_friend in enumerate(friendships[5])
                  if is_friend]
print '\r:::friends_of_five'
print friends_of_five
