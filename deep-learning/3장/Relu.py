import numpy as np

def relu(x):
    return np.maximum(0, x)

# 테스트
x = np.array([-2, -1, 0, 1, 2])
print(relu(x))  # 출력: array([0, 0, 0, 1, 2])

