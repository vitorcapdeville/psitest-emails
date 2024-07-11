import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Annotated
from urllib.parse import unquote_plus

import httpx
from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException

from app.model import EmailData
from app.settings import Settings, get_settings

app = FastAPI()


def send_email(receiver_email: str, subject: str, message: str, sender_password: str):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "vitor771@gmail.com"

    # Cria uma mensagem MIME com UTF-8
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    body = MIMEText(message, "plain", "utf-8")
    msg.attach(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


@app.post("/send-email")
async def enviar_email(
    data: EmailData,
    settings: Annotated[Settings, Depends(get_settings)],
    background_tasks: BackgroundTasks,
):
    headers = {
        "User-ID": settings.NEUTRINO_ID,
        "API-Key": settings.NEUTRINO_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.NEUTRINO_URL}/email-validate?email={data.email}", headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json()["api-error-msg"])
    if not response.json()["valid"]:
        raise HTTPException(status_code=400, detail="Invalid email")

    background_tasks.add_task(
        send_email, unquote_plus(data.email), data.subject, data.message, settings.GOOGLE_APP_PASS
    )
