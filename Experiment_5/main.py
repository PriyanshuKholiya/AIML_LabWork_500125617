import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("sample_dataset.csv")

# 1. Age Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Age', data=data)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 2. Score Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Score', data=data)
plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 3. Height Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['Height(cm)'], bins=10, kde=True)
plt.title('Height Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Weight Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['Weight(kg)'], bins=10, kde=True)
plt.title('Weight Distribution')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(data[['Age', 'Height(cm)', 'Weight(kg)', 'Score']].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
