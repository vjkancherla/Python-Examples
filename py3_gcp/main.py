#!/usr/bin/env python3

import os
import base64
import smtplib
from email.message import EmailMessage
from google.cloud import secretmanager

PROJECT_ID        = os.environ.get("GCP_PROJECT", "")
MAIL_FROM         = os.environ.get("MAIL_FROM", "").strip()
MAIL_TO           = os.environ.get("MAIL_TO", "").strip()
MAIL_SUBJECT      = os.environ.get("MAIL_SUBJECT", "").strip()
MAILJET_SECRET_ID = os.environ.get("MAILJET_SECRET_ID", "").strip()

def access_secret():
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{PROJECT_ID}/secrets/{MAILJET_SECRET_ID}/versions/latest"

    response = client.access_secret_version(name=name)

    return response.payload.data.decode("UTF-8")


def send_email_notification(event, context):
    print(f"BEGIN messageId {context.event_id} published at {context.timestamp}")

    secret_value = access_secret()

    secrets = secret_value.split()

    mailServer    = secrets[1]
    mailPort      = secrets[3]
    mailUsrName   = secrets[5]
    mailUsrPwd    = secrets[7]
    mailLocalHost = "toolstation.com"


    if "data" in event:
        mailMessageBody = base64.b64decode(event["data"]).decode("utf-8")
    else:
        mailMessageBody = ""

    outboundMessage = EmailMessage()
    outboundMessage.set_content(mailMessageBody)
    outboundMessage["Subject"] = MAIL_SUBJECT
    outboundMessage["From"] = MAIL_FROM
    outboundMessage["To"] = MAIL_TO

    print(f"mailServer: {mailServer}, mailPort: {mailPort}")

    smtpServer = smtplib.SMTP(host=mailServer, port=mailPort, local_hostname=mailLocalHost)

    #smtpServer.set_debuglevel(2)

    smtpServer.starttls()

    smtpServer.ehlo()

    smtpServer.login(mailUsrName, mailUsrPwd)

    smtpServer.send_message(outboundMessage)

    smtpServer.quit()

    print(f"END messageId {context.event_id}")
