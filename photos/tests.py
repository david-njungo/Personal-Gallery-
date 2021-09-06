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