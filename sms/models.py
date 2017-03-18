from django.db import models


class Key(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    active = models.BooleanField(default=True)
