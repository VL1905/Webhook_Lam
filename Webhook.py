from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Thay thế bằng token bot Telegram của bạn
TOKEN = "7810118093:AAGusdSvdjd4fNbTrB5BUK-GXkY1bdJFMEQ"
CHAT_ID = "5900286005"

@app.route("/", methods=["GET", "POST", "HEAD"])  # Thêm HEAD
def webhook():
    if request.method == "HEAD":
        return "", 200  # Trả về mã 200 cho HEAD request

    if request.method == "GET":
        return "Webhook is running!", 200

    if request.method == "POST":
        data = request.json
        message = data.get("message", "Không có nội dung")
        send_telegram_message(message)
        return jsonify({"status": "ok"}), 200

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

