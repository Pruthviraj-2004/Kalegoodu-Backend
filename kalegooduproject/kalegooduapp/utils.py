from twilio.rest import Client
from django.conf import settings

def send_whatsapp_message(to_number, body):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=f'whatsapp:{to_number}',
        from_=settings.TWILIO_WHATSAPP_NUMBER,
        body=body
    )
    return message.sid