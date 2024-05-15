import pandas as pd
import os

def merge_csv_files_in_directory(directory_path, primary_key, base_file_name, output_file_path):
    # Load the main base file (cemeteries.csv)
    base_df = pd.read_csv(os.path.join(directory_path, base_file_name))

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv') and filename != base_file_name:
            file_path = os.path.join(directory_path, filename)
            try:
                # Load the current CSV file
                current_df = pd.read_csv(file_path)
                
                # Merge the current CSV with the base DataFrame
                base_df = pd.merge(base_df, current_df, on=primary_key, how="left", suffixes=('', '_merged'))
                
                # Combine overlapping columns
                for col in current_df.columns:
                    if col != primary_key and '_merged' in col:
                        original_col = col.replace('_merged', '')
                        if original_col in base_df.columns:
                            base_df[original_col] = base_df[original_col].combine_first(base_df[col])
                        base_df.drop(columns=[col], inplace=True)

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Save the merged DataFrame to a new CSV file
    base_df.to_csv(output_file_path, index=False)
    print(f"Merged file saved to {output_file_path}")

# Example usage
directory_path = '.'  # Current directory
primary_key = 'pkoakwood'
base_file_name = 'cemeteries.csv'
output_file_path = 'updated_cemeteries.csv'
merge_csv_files_in_directory(directory_path, primary_key, base_file_name, output_file_path)
