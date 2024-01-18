import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('.\\3rd-Sem_Lab_Work\\Week11\\demo.csv')

# Display initial data info
print("Initial Data Info:")
print(data.info())
print("\nData Head:\n", data.head())

# Step (a): Clean independent features
# Assuming 'x1' and 'x2' have nominal data, encode them
label_encoders = {}
for col in ['x1', 'x2']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Step (b): Add one more feature x7 with values between 0 and 1
# Generating random values between 0 and 1 for the new feature x7
data['x7'] = np.random.rand(data.shape[0])

# Step (c): Perform scaling
# Separating independent variables (X) and the dependent variable (y)
X = data.drop('y', axis=1)
y = data['y']

# Scaling continuous variables (x3 through x7) only
scaler = StandardScaler()
X[['x3', 'x4', 'x5', 'x6', 'x7']] = scaler.fit_transform(X[['x3', 'x4', 'x5', 'x6', 'x7']])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step (d): Train dataset using Logistic Regression, Decision Tree, and Random Forest
# Initialize models
log_reg = LogisticRegression()
dec_tree = DecisionTreeClassifier()
rand_forest = RandomForestClassifier()

# Train models
log_reg.fit(X_train, y_train)
dec_tree.fit(X_train, y_train)
rand_forest.fit(X_train, y_train)

# Predictions
y_pred_log_reg = log_reg.predict(X_test)
y_pred_dec_tree = dec_tree.predict(X_test)
y_pred_rand_forest = rand_forest.predict(X_test)

# Step (d): Compare models based on accuracy and F1 score
models = {
    "Logistic Regression": (y_pred_log_reg, log_reg),
    "Decision Tree": (y_pred_dec_tree, dec_tree),
    "Random Forest": (y_pred_rand_forest, rand_forest)
}

print("\nModel Performance:")
for model_name, (y_pred, model) in models.items():
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"{model_name} - Accuracy: {accuracy:.4f}, F1 Score: {f1:.4f}")

# Step (e): Draw confusion matrix for each model
plt.figure(figsize=(18, 5))
for i, (model_name, (y_pred, model)) in enumerate(models.items(), 1):
    cm = confusion_matrix(y_test, y_pred)
    plt.subplot(1, 3, i)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix for {model_name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
plt.tight_layout()
plt.show()
