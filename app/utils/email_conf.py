from fastapi_mail import ConnectionConfig

config = ConnectionConfig(
    MAIL_USERNAME="d29654d8799c88",
    MAIL_PASSWORD="e0dea2231d48ae",
    MAIL_FROM="from@example.com",
    MAIL_PORT=587,
    MAIL_SERVER="sandbox.smtp.mailtrap.io",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
) 