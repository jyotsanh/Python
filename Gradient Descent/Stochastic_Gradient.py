import numpy as np 
from sklearn.datasets import load_diabetes
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = load_diabetes()
x = df.data 
y = df.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)


lr = LinearRegression()
lr.fit(x_train,y_train)
print("Model coef: ",lr.coef_)
print("model intercept_ : ",lr.intercept_)
Y = lr.predict(x_test)

class Stochastic:
	def __init__(self,learning_rate=0.01,epochs=100):
		self.lr = learning_rate
		self.ep = epochs
		self.intercept_ = 0
		self.coef_ = None
	def fit(self,x_train,x_test):
		self.coef_ = np.ones(x_train.shape[1])

		for i in range(self.ep):
			for j in range(x_train.shape[0]):
				rom = np.random.randint(0,x_train.shape[0])

				y_hat = np.dot(x_train[rom],self.coef_) + self.intercept_
				slope_inter = -2*(y_train[rom] - y_hat)
				slope_coef = -2*np.dot((y_train[rom] - y_hat),x_train[rom])
				self.coef_ = self.coef_ - self.lr*slope_coef
				self.intercept_ = self.intercept_ - self.lr*slope_inter
		print(self.ep,self.intercept_)


	def predict(self,x_test):
		y_pred = np.dot(x_test,self.coef_) + self.intercept_
		return y_pred


Sgd = Stochastic(0.01,100)
Sgd.fit(x_train,y_train)
y_p = Sgd.predict(x_test)
print("model accuracy : ",r2_score(y_test,Y))
print("my acuuracy: ",r2_score(y_test,y_p))
