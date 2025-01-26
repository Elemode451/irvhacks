import pandas as pd
from app.datasets.paths import GENERAL_DATASET

def query_general_dataset(first_name, last_name):
    """
    Query an Excel spreadsheet to find details about a specific physician.

    Args:
        file_path (str): Path to the Excel file.
        first_name (str): The physician's first name.
        last_name (str): The physician's last name.

    Returns:
        pd.DataFrame: Filtered rows matching the query.
    """
    try:
        # Load the Excel spreadsheet
        data = pd.read_excel(GENERAL_DATASET)

        # Query the DataFrame
        filtered_data = data[
            (data['covered_recipient_first_name'] == first_name) &
            (data['covered_recipient_last_name'] == last_name)
        ]

        return filtered_data

    except FileNotFoundError:
        print(f"Error: File not found at {GENERAL_DATASET}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


