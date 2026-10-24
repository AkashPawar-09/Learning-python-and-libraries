import numpy as np


# numpy.random.rand() is a NumPy function used to generate random numbers between 0 and 1 
# and store them in an array of a specified shape

x = np.random.rand()
print(x)

# ------------------------------------------------------------------------------------------------------

# generates a one-dimensional array containing 5 random values between 0 and 1.

import numpy as np
arr = np.random.rand(5)
print(arr)                      # [0.3708346  0.90490661 0.68008828 0.68483772 0.64202762]


import numpy as np
arr = np.random.rand(3, 4)
print(arr)

"""
[[0.13732672 0.19149167 0.68809934 0.67822412]
[0.86304425 0.36661701 0.6169331  0.86790626]
[0.3203552  0.04287939 0.19238803 0.79719994]]
"""
#  np.random.rand(3, 4) generates a 3×4 matrix, where each element is a random value between 0 and 1.

# ------------------------------------------------------------------------------------------------------

# to generate a 3D array of shape (2, 2, 2) using random values.

arr = np.random.rand(2, 2, 2)
print(arr)

"""     2D array

[[[0.42434422 0.07644954]
  [0.39373168 0.45539157]]

 [[0.73175903 0.11979302]
  [0.53320335 0.8540258 ]]]

"""
