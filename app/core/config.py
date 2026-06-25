import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# SUPABASE
# ==========================================

SUPABASE_URL = os.getenv(
    "SUPABASE_URL"
)

SUPABASE_SERVICE_ROLE_KEY = os.getenv(
    "SUPABASE_SERVICE_ROLE_KEY"
)

# ==========================================
# JWT
# ==========================================

JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY"
)

JWT_ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        1440
    )
)

# ==========================================
# EMAIL
# ==========================================

MAIL_USERNAME = os.getenv(
    "MAIL_USERNAME"
)

MAIL_PASSWORD = os.getenv(
    "MAIL_PASSWORD"
)

MAIL_FROM = os.getenv(
    "MAIL_FROM"
)

MAIL_PORT = int(
    os.getenv(
        "MAIL_PORT",
        587
    )
)

MAIL_SERVER = os.getenv(
    "MAIL_SERVER",
    "smtp.gmail.com"
)

MAIL_FROM_NAME = os.getenv(
    "MAIL_FROM_NAME",
    "Expense Tracker"
)

MAIL_STARTTLS = os.getenv(
    "MAIL_STARTTLS",
    "True"
).lower() == "true"

MAIL_SSL_TLS = os.getenv(
    "MAIL_SSL_TLS",
    "False"
).lower() == "true"

USE_CREDENTIALS = os.getenv(
    "USE_CREDENTIALS",
    "True"
).lower() == "true"

VALIDATE_CERTS = os.getenv(
    "VALIDATE_CERTS",
    "True"
).lower() == "true"