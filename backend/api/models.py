from django.db import models

# Create your models here.

class TODO(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=255)
    isDone = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title