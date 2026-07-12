import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

import fear_greed
import gspread
from google.oauth2.service_account import Credentials

# -------------------------
# Fear & Greed Index取得
# -------------------------
data = fear_greed.get()
score = round(data["score"])  # CNN表示に合わせて整数化

print(f"FGI: {score}")

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
# 更新日時（日本時間）
# -------------------------
now = datetime.now(
    ZoneInfo("Asia/Tokyo")
).strftime("%Y-%m-%d %H:%M")

# -------------------------
# E2=更新日時
# F2=FGI
# -------------------------
worksheet.update(
    "E2:F2",
    [[now, score]]
)

print(f"Updated: {now}  FGI={score}")
