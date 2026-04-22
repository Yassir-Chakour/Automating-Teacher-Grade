from dotenv import load_dotenv
from pathlib import Path
import gspread
import os

load_dotenv()

ROOT_DIR = Path(__file__).parent.parent.parent
CREDENTIALS_PATH = os.path.join(ROOT_DIR, 'credentials.json')

def google_client():
    """
    Connects to Google Sheets and returns the spreadsheet object.
    """
    gc = gspread.service_account(filename=CREDENTIALS_PATH)
    spreadsheet_id = os.getenv('SPREADSHEET_ID')
    sh = gc.open_by_key(spreadsheet_id)

    return sh