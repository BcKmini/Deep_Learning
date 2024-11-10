import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 실제로 넘파이 배열을 제대로 처리 했는지 확인
x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))
# 출력: array([0.26894142, 0.73105858, 0.88079708])

# 넘파이 -> 브로드캐스트 기능
t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
# 출력: array([2., 3., 4.])
print(1.0 / t)
# 출력: array([1. , 0.5 , 0.33333333])
