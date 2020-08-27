from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting


# Create your models here.
@register_setting
class Header(BaseSetting):
    color = models.CharField(max_length=100, blank=False, null=False)
    is_creatable = False
