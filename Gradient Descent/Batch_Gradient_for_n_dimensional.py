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
print(lr.intercept_,lr.coef_)
Y = lr.predict(x_test)

class Batch:
	def __init__(self,learning_rate=0.01,epochs=100):
		self.lr = learning_rate
		self.ep = epochs
		self.intercept_ = 0
		self.coef_ = None
	def fit(self,x_train,y_train):
		self.coef_ = np.ones(x_train.shape[1])

		for i in range(self.ep):
			y_hat = np.dot(x_train,self.coef_) + self.intercept_

			#slopes

			slope_inter = -2*np.sum(y_train-y_hat)/(x_train.shape[0])
			slope_coef = -2*np.dot((y_train-y_hat),x_train)/(x_train.shape[0])

			#optimizing

			self.coef_ = self.coef_ - self.lr*slope_coef
			self.intercept_ = self.intercept_ - self.lr*slope_inter
		print(self.intercept_,self.coef_)
	def predict(self,x_test):
		y_pred = np.dot(x_test,self.coef_) + self.intercept_
		return y_pred


gd = Batch(0.09,10000)
gd.fit(x_train,y_train)
y_p = gd.predict(x_test)
print("model accuracy : ",r2_score(y_test,Y))
print("my acuuracy: ",r2_score(y_test,y_p))