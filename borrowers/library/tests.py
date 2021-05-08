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

    def test_about(self):
        response = self.c.get(reverse('library-about'))
        expected_html = render_to_string('about.html')
        assert "Who are we?" in expected_html
        assert "about.html" in [t.name for t in response.templates]

    def test_show(self):
        response = self.c.get('library-show')
        assert "404.html" in [t.name for t in response.templates]

class TestLoggedInViews(BaseTestCase):

    def setUp(self):
        self.c = Client()
        self.c.login(username="testuser", password="testpass")

    def test_books_page_load(self):
        response = self.c.get(reverse('library-books'))
        assert "booklist" in response.context
        assert response.context['booklist'].count() == 1
        assert "books.html" in [t.name for t in response.templates]

    def test_create_page_load(self):
        response = self.c.get(reverse('books-create'))
        assert "newbook.html" in [t.name for t in response.templates]

    # def test_create_new_book(self):
    #     response = self.c.post(reverse('books-create'), {
    #         'name': 'new_test_book',
    #         'author': self.test_author.id
    #     })
    #     assert Book.objects.filter(name='new_test_book').exists()

    def test_show_page_load(self):
        response = self.c.get(reverse('library-show', kwargs={'book_id': self.book.id}))
        assert "show.html" in [t.name for t in response.templates]