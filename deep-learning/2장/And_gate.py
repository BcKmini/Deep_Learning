# 간단한 구현 AND함수
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

# 매개변수 w1, w2, theta는 함수 안에서 초기화 하고 가중치를 곱한 
# 임게값을 넘으면 1, 그 외에는 0을 반환

# 출력
print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))

'''출력값
0
0
0
1
'''

# 가중치에 편향 도입 
import numpy as np
x = np.array([0, 1]) #입력
w = np.array([0.5, 0.5]) #가중치
b = -0.7 #편향
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x) + b)

# 가중치와 편향 구현하기
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else: 
        return 1
    
'''
가중치와 편향 계산: tmp = np.sum(w*x) + b는 가중치와 입력을 곱하고 그 합에 편향 b를 더한 값입니다.
np.sum(w*x)에서 w와 x의 각 요소를 곱하고 그 결과를 더하여 하나의 값으로 만듭니다. 이 값에 편향 b를 더하여 최종 값을 얻습니다.

출력 결정: tmp 값이 0보다 작거나 같으면 0을, 그렇지 않으면 1을 반환합니다.
즉, tmp 값이 임계값(0)을 넘지 않으면 0, 넘으면 1로 출력합니다.
'''

print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))
