from django.db import models

# Create your models here.
class Image(models.Model):
    # article_image = models.ImageField(upload_to = '')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    link = models.CharField(max_length = 150)   

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name =models.CharField(max_length = 30)

    def __str__(self):
        return self.name   