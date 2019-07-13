import uuid

from django.conf inport settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer

from animal_lib.notifications.models import Notification, notification_handler

# Create your models here.
