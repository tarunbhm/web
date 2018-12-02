from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Notification(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    to_user_id = models.IntegerField()
    from_user_id = models.IntegerField()
    CTA_URL = models.URLField(max_length=255, null=True)
    CTA_Text = models.CharField(max_length=255)
    message_html = models.CharField(max_length=255, null=True, help_text=_("Html message"))
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.notification
