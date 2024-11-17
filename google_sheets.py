import gspread
from google.auth import default
import pandas as pd

def get_google_sheets_client():
    creds, _ = default()
    return gspread.authorize(creds)

def load_google_sheet(sheet_id, sheet_range):
    client = get_google_sheets_client()
    sheet = client.open_by_key(sheet_id)
    worksheet = sheet.get_worksheet(0)
    data = worksheet.get(sheet_range)
    return pd.DataFrame(data[1:], columns=data[0])

def upload_to_google_sheet(df, sheet_id, sheet_name):
    client = get_google_sheets_client()
    sheet = client.open_by_key(sheet_id)
    try:
        worksheet = sheet.worksheet(sheet_name)
    except:
        worksheet = sheet.add_worksheet(title=sheet_name, rows="100", cols="20")
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
