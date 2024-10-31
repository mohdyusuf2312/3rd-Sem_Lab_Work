import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Step 1: Generate random values for x1 and x2
np.random.seed(42)  # For reproducibility
x1 = np.random.rand(1000)
x2 = np.random.rand(1000)

# Step 2: Generate random values for c
c = np.random.rand(1000)

# Step 3: Calculate y based on the function
y = x1**2 + 3 * x2 + c

# Combine x1 and x2 into a single feature matrix
X = np.column_stack((x1, x2))

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Transform the features to polynomial features
poly = PolynomialFeatures(degree=2)  # Degree 2 for quadratic polynomial
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Step 6: Train the Polynomial Regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Step 7: Make predictions
y_pred = model.predict(X_test_poly)

# Step 8: Calculate the score of the model
score = r2_score(y_test, y_pred)

# Display the result
print(f"R^2 Score of the Polynomial Regression model: {score:.4f}")
