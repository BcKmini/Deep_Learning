import numpy as np
from tensorflow.keras.datasets import mnist

def load_mnist(flatten=True, normalize=False):
    
    # Keras에서 MNIST 데이터셋 로드
    (x_train, t_train), (x_test, t_test) = mnist.load_data()

    # 정규화
    if normalize:
        x_train = x_train.astype(np.float32) / 255.0
        x_test = x_test.astype(np.float32) / 255.0

    # 평탄화
    if flatten:
        x_train = x_train.reshape(x_train.shape[0], -1)
        x_test = x_test.reshape(x_test.shape[0], -1)

    return (x_train, t_train), (x_test, t_test)
