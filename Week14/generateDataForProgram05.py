import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate continuous independent features
x1 = np.random.normal(loc=50, scale=10, size=1000)  # Normal distribution
x2 = np.random.uniform(low=0, high=100, size=1000)  # Uniform distribution
x3 = np.random.exponential(scale=30, size=1000)      # Exponential distribution
x4 = np.random.beta(a=2, b=5, size=1000) * 100       # Beta distribution scaled to [0, 100]

# Generate nominal feature (x5)
x5 = np.random.choice(['A', 'B', 'C', 'D'], size=1000)  # Four categories

# Generate dependent feature (y) based on a simple rule
# Here we assume a simple condition for generating y
y = np.where((x1 + x2) / 2 > 50, 1, 0)  # y is 1 if average of x1 and x2 > 50, else 0

# Create DataFrame
data = pd.DataFrame({
    'x1': x1,
    'x2': x2,
    'x3': x3,
    'x4': x4,
    'x5': x5,
    'y': y
})

# Save to CSV
data.to_csv('temp.csv', index=False)

print("Synthetic dataset 'temp.csv' has been created.")
