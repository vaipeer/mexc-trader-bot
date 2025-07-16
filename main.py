from flask import Flask, request
import requests

app = Flask(__name__)

# جایگزین کن با توکن خودت
TELEGRAM_TOKEN = '7287941986:AAGrNq_aNdiDiGvLhfKT5M6-vm1ZamegQZA'
TELEGRAM_CHAT_ID = '@mexccccccc'

@app.route("/")
def home():
    return "✅ Mexc Bot is Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    signal = data.get("signal")
    pair = data.get("pair", "BTCUSDT")

    if signal == "buy":
        send_telegram(f"📈 Buy Signal for {pair}")
    elif signal == "sell":
        send_telegram(f"📉 Sell Signal for {pair}")
    else:
        send_telegram(f"❓ Unknown Signal Received: {data}")
    
    return "ok"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


