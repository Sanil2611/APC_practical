from sklearn.linear_model import LinearRegression
import numpy as np

# Tiny illustrative dataset: study hours and marks.
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([35, 42, 50, 63, 70])

model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[6]])
print("Predicted mark for 6 study hours:", round(predicted[0], 2))
