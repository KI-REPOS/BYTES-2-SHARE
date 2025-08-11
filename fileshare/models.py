from django.db import models
from django.contrib.auth.models import User

class SharedFile(models.Model):
    file = models.FileField(upload_to='')
    filename = models.CharField(max_length=255)
    size = models.BigIntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.filename
