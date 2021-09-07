from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name 

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    link = models.CharField(max_length = 150)     

    def save_Image(self):
        self.save()

    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    @classmethod
    def category(cls):
        category = cls.objects.all()
        return category

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
 