from django.db import models

class Channel(models.Model):
    link = models.TextField(max_length=500)
    subscriber = models.TextField(max_length=10)
    keyword = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.link