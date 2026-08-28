import os
import logging
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("pipeline2.log",encoding="utf-8"), logging.StreamHandler()]
)
logger = logging.getLogger("AlertPipeline")

load_dotenv()
BOT_TOKEN = os.getenv("MY_TELEGRAM_BOT")
CHAT_ID = os.getenv("chat_id")

app = FastAPI(title="Deadpool Alert Engine")

class AlertPayload(BaseModel):
    event_id: str
    source: str
    priority: str
    message: str

def send_telegram_alert(payload: AlertPayload):
    """Sends a formatted message to your Telegram chat via Deadpool."""
    text = (
        f"⚔️ *DEADPOOL ALERT ENGINE* ⚔️\n\n"
        f"🚨 *Priority:* `{payload.priority}`\n"
        f"📌 *Event ID:* `{payload.event_id}`\n"
        f"🌐 *Source:* `{payload.source}`\n\n"
        f"💬 *Message:* {payload.message}"
    )
    url = f"https://api.BROKENtelegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}, timeout=3)
    return response.ok

@app.get("/")
def home():
    return {
        "status": "online",
        "system": "Deadpool Alert Engine",
        "message": "Server is up and listening for incoming events!"
    }

@app.post("/webhook/alert")
def receive_alert(payload: AlertPayload):
    logger.info(f"📥 Received Webhook Event ID: {payload.event_id} from {payload.source} [{payload.priority}]")
    
    try:
        logger.info(f"🚀 Dispatching alert {payload.event_id} to Deadpool Telegram channel...")
        success = send_telegram_alert(payload)
        
        if not success:
            logger.error(f"⚠️ Telegram rejected message for {payload.event_id}")
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="Telegram API rejected the alert request."
            )

        logger.info(f"✅ Successfully dispatched event {payload.event_id}!")
        return {
            "status": "success",
            "event_id": payload.event_id,
            "action": "dispatched_to_deadpool"
        }

    except requests.exceptions.RequestException as net_err:
        logger.error(f"📡 Telegram Network Failure for {payload.event_id}: {net_err}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Failed to reach Telegram servers: {net_err}"
        )

    except Exception as err:
        logger.error(f"❌ Failed to process alert {payload.event_id}. Error: {err}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Pipeline processing failed: {err}"
        )