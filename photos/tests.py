from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(name = 'food')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
     # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(name = 'Nairobi')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
     # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new category and saving it
        self.category = Category(name = 'food')
        self.category.save_category()

        # Creating a new location and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save()

        self.new_image= Image(name = '',description = '',link = '',Category= self.category)
        self.new_image.save()

        self.new_image.location.add(self.new_location)

    def tearDown(self):
        Category.objects.all().delete()
        Image.objects.all().delete()
        Location.objects.all().delete()