from django.db import models

class GiphyCalendar(models.Model):
    date = models.DateField(primary_key=True)
    url = models.URLField(max_length=2083)
    giphy = models.BinaryField(max_length=100*1024*1024)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description