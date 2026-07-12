import json
import os

import fear_greed
import gspread
from google.oauth2.service_account import Credentials

# -------------------------
# Fear & Greed Index取得
# -------------------------
data = fear_greed.get()
score = round(data["score"])

print("FGI:", score)

# -------------------------
# Google認証
# -------------------------
service_account = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT"])

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

credentials = Credentials.from_service_account_info(
    service_account,
    scopes=scopes
)

gc = gspread.authorize(credentials)

# -------------------------
# スプレッドシートを開く
# -------------------------
SPREADSHEET_ID = "1iJNyzVfgRP8E_Y0qAF7NSMkwJmnRbgPRRduYi6vjyYE"

worksheet = gc.open_by_key(
    SPREADSHEET_ID
).worksheet("FGI")

# -------------------------
# F2へ書き込み
# -------------------------
worksheet.update(
    "F2",
    [[score]]
)

print("Google Sheets Updated!")
