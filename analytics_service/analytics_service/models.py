from django.db import models

class Analytics(models.Model):
    service_name = models.CharField(max_length=100)
    request_count = models.IntegerField(default=0)

    def __str__(self):
        return self.service_name
