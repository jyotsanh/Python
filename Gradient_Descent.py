import numpy as np 
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



x,y = make_regression(n_samples=100,n_features=1,n_targets=1,noise=20)
plt.scatter(x,y)
plt.show()

lr = LinearRegression()
lr.fit(x,y)
print(f" m = {lr.coef_},b = {lr.intercept_}")


class Gradient:
	def __init__(self,learning_rate,epochs):
		self.lr = learning_rate
		self.epochs = epochs
		self.m = 100
		self.b = 20
	def fit(self,x_train,y_train):
		for i in range(self.epochs):
			slope_b = -2*np.sum(y_train - self.m*x_train.reshape(-1)-self.b)
			slope_m = -2*np.sum((y_train - self.m*x_train.reshape(-1) - self.b)*x_train.reshape(-1))
			self.m = self.m - self.lr*slope_m
			self.b = self.b - self.lr*slope_b
			print(f"{i+1} epochs , m = {self.m} , b = {self.b}")

gd = Gradient(0.001,30)
gd.fit(x,y)