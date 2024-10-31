import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay

# Load the dataset
df = pd.read_csv('.\\3rd-Sem_Lab_Work\\Week14\\temp.csv')

# Step a: Clean independent features
# Check for missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Check data types
print("\nData types:")
print(df.dtypes)

# Impute missing values if any
# Handle numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Handle nominal (categorical) column
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Verify that there are no more missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Convert categorical variables to numeric using one-hot encoding
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Step b: Draw heatmap to show correlations among independent features
plt.figure(figsize=(10, 6))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Step c: Train the dataset using Logistic Regression, Decision Tree, and Random Forest
# Prepare the data
X = df.drop(columns=['y'])  # Drop the dependent variable from features
y = df['y']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

# Train and evaluate each model
results = {}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    results[model_name] = {'Accuracy': accuracy, 'F1 Score': f1}
    
    # Draw confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap='Blues')
    plt.title(f'Confusion Matrix: {model_name}')
    plt.show()

# Show performance comparison
results_df = pd.DataFrame(results).T
print("Model Performance Comparison:")
print(results_df)

# Step e: Check whether scaling improves performance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize models again for scaled data
scaled_results = {}

for model_name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred_scaled = model.predict(X_test_scaled)
    accuracy_scaled = accuracy_score(y_test, y_pred_scaled)
    f1_scaled = f1_score(y_test, y_pred_scaled)
    scaled_results[model_name] = {'Accuracy': accuracy_scaled, 'F1 Score': f1_scaled}

# Show performance comparison for scaled data
scaled_results_df = pd.DataFrame(scaled_results).T
print("\nModel Performance Comparison with Scaling:")
print(scaled_results_df)
