import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/sarah/Downloads/Ice Cream.csv")
print(data)
x = data.iloc[:, 0]
y = data.iloc[:, 1]
plt.scatter(x, y)
plt.show()
x = np.array(x).reshape((len(x), 1))
y = np.array(y).reshape((len(y), 1))
x_new = np.hstack((np.ones(shape=(len(x), 1)), x))
w = np.random.rand(2, 1)
learning_rate = float(input("Learning Rate : "))
k = int(input("How many times for training: "))
for i in range(k):
    h = x_new @ w
    E = h - y
    w = w - (learning_rate / len(x)) * (x_new.T @ E)
t = np.arange(start=0, stop=50, step=1)
predict = w[0][0] + w[1][0] * t
plt.scatter(x, y)
plt.plot(t, predict, color="black")
plt.show()