from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    fullname = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    rdate = models.DateField()

    def __str__(self):
        return self.fullname