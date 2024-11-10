import numpy as np

def step_function(x):
    y = x > 0
    return y.astype(int)  # np.int 대신 int 사용

x = np.array([-1, 1.0, 2.0])
y = step_function(x)
y
