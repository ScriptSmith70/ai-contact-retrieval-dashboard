# data_processing.py
import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def load_csv(uploaded_file):
    """Load CSV data and return as a DataFrame."""
    return pd.read_csv(uploaded_file)

def save_to_google_sheets(sheet_id, sheet_range, data):
    """Save extracted information to a Google Sheet."""
    try:
        creds = service_account.Credentials.from_service_account_file(
            os.getenv("GOOGLE_SHEETS_CREDENTIALS")
        )
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        values = [list(row.values()) for row in data.to_dict(orient='records')]
        body = {'values': values}
        
        sheet.values().update(
            spreadsheetId=sheet_id,
            range=sheet_range,
            valueInputOption="RAW",
            body=body
        ).execute()
    except Exception as e:
        st.error(f"Error saving to Google Sheets: {e}")
