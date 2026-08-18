import os
import time
import requests

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("BOT_TOKEN missing")
    while True:
        time.sleep(60)

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

print("Rathore AI Bot started...")

offset = 0

while True:
    try:
        response = requests.get(
            url,
            params={"timeout": 30, "offset": offset},
            timeout=35
        )

        data = response.json()

        for update in data.get("result", []):
            offset = update["update_id"] + 1

            message = update.get("message", {})
            chat = message.get("chat", {})
            text = message.get("text", "")

            if text == "/start":
                requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                    data={
                        "chat_id": chat["id"],
                        "text": "🤖 Rathore AI Bot चालू है!\n\nSignal system जल्द तैयार होगा."
                    }
                )

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
