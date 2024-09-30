import pandas as pd

def import_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file name.")
        return None

def export_data(data, file_name):
    data.to_csv(file_name, index=False)
    print(f"Data successfully exported to {file_name}")

def show_dataset_details(data):
    if data is not None:
        print("Number of rows and columns:", data.shape)
        print("\nFirst five rows:\n", data.head())
        print("\nSize of the dataset (number of elements):", data.size)
        print("\nNumber of missing values:\n", data.isnull().sum())

        numerical_columns = data.select_dtypes(include='number').columns
        if not numerical_columns.empty:
            print("\nSummary statistics for numerical columns:")
            print("Sum:\n", data[numerical_columns].sum())
            print("\nAverage:\n", data[numerical_columns].mean())
            print("\nMinimum values:\n", data[numerical_columns].min())
            print("\nMaximum values:\n", data[numerical_columns].max())
        else:
            print("\nNo numerical columns found.")
    else:
        print("Data not available to show details.")


if __name__ == "__main__":
    file_name = 'sample_dataset.csv' 

    data = import_data(file_name)
    
    show_dataset_details(data)
    
    export_file_name = 'exported_sample_dataset.csv'  
    export_data(data, export_file_name)
