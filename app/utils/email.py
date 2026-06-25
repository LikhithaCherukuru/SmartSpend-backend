from fastapi_mail import (
    FastMail,
    MessageSchema,
    ConnectionConfig
)

from app.core.config import (
    MAIL_USERNAME,
    MAIL_PASSWORD,
    MAIL_FROM,
    MAIL_PORT,
    MAIL_SERVER,
    MAIL_FROM_NAME,
    MAIL_STARTTLS,
    MAIL_SSL_TLS,
    USE_CREDENTIALS,
    VALIDATE_CERTS
)
print("MAIL_USERNAME =", MAIL_USERNAME)
print("MAIL_PASSWORD =", MAIL_PASSWORD)
conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_FROM=MAIL_FROM,
    MAIL_PORT=MAIL_PORT,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_FROM_NAME=MAIL_FROM_NAME,
    MAIL_STARTTLS=MAIL_STARTTLS,
    MAIL_SSL_TLS=MAIL_SSL_TLS,
    USE_CREDENTIALS=USE_CREDENTIALS,
    VALIDATE_CERTS=VALIDATE_CERTS
)

async def send_reset_email(
    email: str,
    code: str
):
    message = MessageSchema(
        subject="SmartSpend Password Reset Code",
        recipients=[email],
        body=f"""
Your SmartSpend password reset code is:

{code}

This code expires in 10 minutes.
        """,
        subtype="plain"
    )

    fm = FastMail(conf)

    await fm.send_message(message)