from django.db import models

# Create your models here.
class Image(models.Model):
    # article_image = models.ImageField(upload_to = '')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    link = models.CharField(max_length = 150)   

    def __str__(self):
        return self.name


