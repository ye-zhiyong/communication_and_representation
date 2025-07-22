import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.linspace(-10, 10, 400)

y_relu = relu(x)

plt.figure()

plt.plot(1, 2, 1)
plt.plot(x, y_relu, label='ReLU')
plt.title('ReLU Function')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.legend()


plt.tight_layout()
plt.show()
