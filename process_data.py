import pandas as pd
import os

# Folder containing the data files
data_folder = 'data'

# List of CSV files in the data folder
csv_files = [os.path.join(data_folder, file) for file in os.listdir(data_folder) if file.endswith('.csv')]

# Initialize an empty DataFrame to hold the combined data
combined_data = pd.DataFrame()

# Process each CSV file
for file in csv_files:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file)
    
    # Filter rows where the product is "Pink Morsels"
    df = df[df['product'] == 'Pink Morsels']
    
    # Create the "sales" column
    df['sales'] = df['quantity'] * df['price']
    
    # Keep only the "sales", "date", and "region" columns
    df = df[['sales', 'date', 'region']]
    
    # Append the processed data to the combined DataFrame
    combined_data = pd.concat([combined_data, df])

# Save the combined data to a new CSV file
output_file = 'formatted_output.csv'
combined_data.to_csv(output_file, index=False)

print(f"Data processing complete. Output saved to {output_file}.")
