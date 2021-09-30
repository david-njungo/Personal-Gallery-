from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name 

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    category = models.ForeignKey('Category',on_delete=models.CASCADE) 
    location = models.ForeignKey('Location',on_delete=models.CASCADE) 
    image_upload = models.ImageField(upload_to = 'images/')  

    @classmethod
    def images_displayed(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_images(cls,search_term):
        projects = cls.objects.filter(category__icontains=search_term)
        return projects

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    def save_location(self):
        self.save


 