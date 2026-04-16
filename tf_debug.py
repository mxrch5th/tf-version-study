import tensorflow as tf
import numpy as np

# 문제: TensorFlow를 이용해 상수를 정의하고 덧셈 결과를 출력해야 함
# 아래 코드는 현재 설치된 TensorFlow 버전(2.x)에서 오류를 일으킴
node1 = tf.constant(3.0)
node2 = tf.constant(4.0)

# 이 부분이 핵심 오류 구간 (TensorFlow 1.x 방식의 잔재)
result = node1 + node2

print("결과값:", result.numpy())