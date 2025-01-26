import pandas as pd
import sqlite3
from app.datasets.paths import GENERAL_DB

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
        conn = sqlite3.connect(GENERAL_DB)

        query = """
        SELECT *
        FROM physicians
        WHERE lower(covered_recipient_first_name) = ? AND lower(covered_recipient_last_name) = ?
        """

        result = pd.read_sql_query(query, conn, params=(first_name, last_name))
        return result

    except FileNotFoundError:
        print(f"Error: DB not found at {GENERAL_DB}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


