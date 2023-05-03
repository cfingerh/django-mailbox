from django.dispatch.dispatcher import Signal

try:
  message_received = Signal(providing_args=['message'])
 except:
  # Django 4
  message_received = Signal()
