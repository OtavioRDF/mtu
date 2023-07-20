from app.utils.email_conf import config
from app.entities.schemas import EmailSchema
from fastapi_mail import MessageSchema, MessageType, FastMail

async def simple_send(email: EmailSchema, result: str, configuration: str):
    html = """
    <p>Thanks for using Fastapi-mail</p>
    <p> The result is: """ + result + """</p>
    <p> We have used this configuration: """ + configuration + """</p>
    """
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(config)
    await fm.send_message(message)
    return "OK"