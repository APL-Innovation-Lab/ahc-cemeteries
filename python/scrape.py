import requests
import pandas as pd

def fetch_data(page):
    url = f"https://library.austintexas.gov/ahc/cemeteries/export?page={page}"
    response = requests.get(url)
    try:
        # Using pandas to read tables directly from the HTML content
        data_frames = pd.read_html(response.text)
        if data_frames:
            return data_frames[0]  # Assuming the first table is the one we need
        else:
            return None
    except ValueError:
        return None

def main():
    # Initialize an empty DataFrame to store all fetched data
    all_data = pd.DataFrame()

    # Fetching data from pages 0 to 161
    for page in range(162):
        print(f"Fetching data for page {page}")
        data = fetch_data(page)
        if data is not None:
            all_data = pd.concat([all_data, data], ignore_index=True)
        else:
            print(f"No data was fetched from page {page}")

    # Saving the combined DataFrame to a CSV file
    all_data.to_csv('./cemetery_data_all_pages.csv', index=False)
    print("All data has been saved to cemetery_data_all_pages.csv")

if __name__ == "__main__":
    main()
