import pandas as pd

def split_csv_into_pages(input_file, rows_per_file):
    # Load the data
    data = pd.read_csv(input_file)
    
    # Determine the number of splits needed
    num_splits = (len(data) + rows_per_file - 1) // rows_per_file  # Calculate ceil without math.ceil
    
    # Split the dataframe and save into separate files
    for i in range(num_splits):
        # Calculate start and end indices
        start = i * rows_per_file
        end = start + rows_per_file
        
        # Slice the dataframe
        subset = data[start:end]
        
        # Create the output filename
        output_filename = f"{input_file.split('.')[0]}_page_{i + 1}.csv"
        
        # Save the subset dataframe to a new CSV file with the header
        subset.to_csv(output_filename, index=False)
        print(f"Saved '{output_filename}' with {len(subset)} rows.")
    
    print("CSV file split complete.")

# Use the function on your specific file
split_csv_into_pages('cemetery_data_all_pages.csv', 1000)
