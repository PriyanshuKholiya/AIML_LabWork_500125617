import pandas as pd

# Load the dataset
file_name = 'sample_dataset.csv'
data = pd.read_csv(file_name)

# Display the initial data
print("Initial Data:")
print(data.head())

# 1. Handling Missing Values
# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Fill missing values only for numeric columns
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# 2. Removing Duplicates
# Remove duplicate rows
data.drop_duplicates(inplace=True)

# 3. Correcting Inconsistencies
# Assuming 'Name' is a column that might need standardization
data['Name'] = data['Name'].str.title()  # Capitalize first letter of each name

# 4. Filtering Outliers
# Outlier values are data points that significantly differ from the rest of the observations in a dataset.
if 'Height(cm)' in data.columns:
    Q1 = data['Height(cm)'].quantile(0.25)
    Q3 = data['Height(cm)'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data = data[(data['Height(cm)'] >= lower_bound) & (data['Height(cm)'] <= upper_bound)]

# 5. Data Type Conversion
# Ensure that the 'Age' column is of integer type
data['Age'] = data['Age'].astype(int)

# Display the cleaned data
print("\nCleaned Data:")
print(data.head())

# Export the cleaned dataset
cleaned_file_name = 'cleaned_sample_dataset.csv'
data.to_csv(cleaned_file_name, index=False)
print(f"\nCleaned data exported to {cleaned_file_name}")
