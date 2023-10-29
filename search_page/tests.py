from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

class search_page_test(TestCase):
    def test_search_page_url_is_exist(self):
        response = Client().get('/search/')
        self.assertEqual(response.status_code, 200)

    def test_search_page_using_search_page_template(self):
        response = Client().get('/search/')
        self.assertTemplateUsed(response, 'search.html')

    def test_get_books_json(self):
        user = User.objects.create_user(username="Satoru Gojo")
        user.set_password('sukoshirambosioka')
        user.save()

        client = Client()
        client.login(username='Satoru Gojo', password='sukoshirambosioka')
        response = client.get("/get-books/{}/".format(user.id), follow=True)

        self.assertEqual(response.status_code, 404)

    def test_get_books_price_sorted_json(self):
        user = User.objects.create_user(username="Satoru Gojo")
        user.set_password('sukoshirambosioka')
        user.save()

        client = Client()
        client.login(username='Satoru Gojo', password='sukoshirambosioka')
        response = client.get("/get-books-price-sorted/{}/".format(user.id), follow=True)

        self.assertEqual(response.status_code, 404)

