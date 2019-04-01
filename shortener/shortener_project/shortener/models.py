from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Url(models.Model):
    long_url = models.CharField(max_length=2000)
    short_code = models.CharField(max_length=5, validators=[MinLengthValidator(5)], )
    
    def __str__(self):
        return self.long_url

    