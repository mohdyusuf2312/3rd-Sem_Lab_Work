import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 500

# Generate synthetic data
data = {
    'x1': np.random.choice(['Category1', 'Category2', 'Category3'], size=n_samples),  # Nominal data
    'x2': np.random.choice(['TypeA', 'TypeB'], size=n_samples),                       # Nominal data
    'x3': np.random.normal(loc=50, scale=10, size=n_samples),                         # Continuous data
    'x4': np.random.normal(loc=100, scale=15, size=n_samples),                        # Continuous data
    'x5': np.random.normal(loc=200, scale=20, size=n_samples),                        # Continuous data
    'x6': np.random.normal(loc=300, scale=25, size=n_samples),                        # Continuous data
    'x7': np.random.rand(n_samples),                                                  # Continuous data between 0 and 1
    'y': np.random.choice([0, 1], size=n_samples)                                     # Binary target variable
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('demo.csv', index=False)

print("Synthetic data saved to 'demo.csv'.")
