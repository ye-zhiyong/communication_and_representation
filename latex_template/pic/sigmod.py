import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 示例输入范围
x = np.linspace(-10, 10, 400)

# 计算 Sigmoid 输出
y = sigmoid(x)

# 绘制 Sigmoid 函数图像
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sigmoid Function')
plt.title('Sigmoid Function')
plt.xlabel('x')
plt.ylabel('σ(x)')
plt.legend()
plt.show()
