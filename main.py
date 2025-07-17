from flask import Flask, request
import requests

app = Flask(__name__)

# ⚠️ مقادیر زیر رو حتما با توکن و چت آی‌دی خودت جایگزین کن
TELEGRAM_TOKEN = '7287941986:AAGrNq_aNdiDiGvLhfKT5M6-vm1ZamegQZA'
TELEGRAM_CHAT_ID = '@mexccccccc'

@app.route("/")
def home():
    return "✅ Mexc Bot is Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}
    signal = data.get("signal", "no signal")
    pair = data.get("pair", "BTCUSDT")

    message = f"📢 Signal: {signal.upper()} for {pair}"
    send_telegram(message)

    return "OK"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
