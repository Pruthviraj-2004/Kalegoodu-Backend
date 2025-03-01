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

from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def require_authenticated_user(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        if not request.user or not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        return func(self, request, *args, **kwargs)
    return wrapper
