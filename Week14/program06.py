import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Step 1: Generate 1000 random values for x between 0 and 1
np.random.seed(42)  # For reproducibility
x = np.random.rand(1000)

# Step 2: Generate k from 1000 random values (mean of random values for stability)
k_values = np.random.rand(1000)
k = np.mean(k_values)  # You can also use np.random.choice(k_values) if you want a single k

# Step 3: Calculate y based on the function y = 3x + k
y = 3 * x + k

# Convert to DataFrame for easier manipulation
data = pd.DataFrame({'x': x, 'y': y})

# Step 4: Train a Linear Regression model
X = data[['x']]  # Feature
y = data['y']    # Target

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model and fit it
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate the model's performance
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)

# Output the results
print(f"R² score of the Linear Regression model: {score:.4f}")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
