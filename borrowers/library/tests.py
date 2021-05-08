from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.loader import render_to_string

from .models import Author, Book

# Create your tests here.

class BaseTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.test_author = Author.objects.create(name="Test Author")
        cls.book = Book.objects.create(title="Test Book", author = cls.test_author)
        cls.user = User.objects.create_user('testuser', 'test@user.com', 'testpass')

class TestBasicViews(BaseTestCase):

    c = Client()

    def test_home(self):
        response = self.c.get(reverse('library-home'))
        expected_html = render_to_string('home.html')
        assert "Biblioteca" in expected_html
        assert "home.html" in [t.name for t in response.templates]