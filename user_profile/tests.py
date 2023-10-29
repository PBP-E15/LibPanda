from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from user_profile.models import Biodata, Wallet
from django.contrib.auth.models import User

class user_profile_test(TestCase):
    def test_user_profile_url_is_exist(self):

        response = Client().get('/profile/')
        self.assertEqual(response.status_code, 302)

    def create_biodata(self, name='Satoru Gojo', email="sukoshi@rambo.sioka", gender="male", birthday="1989-12-7", phone_number="0812345678"):
        user = User.objects.create_user(username="Satoru Gojo")
        user.set_password('sukoshirambosioka')
        user.save()
        
        return Biodata.objects.create(user=user, name=name, email=email, gender=gender, birthday=birthday, phone_number=phone_number)

    def create_wallet(self, balance=0):
        user = User.objects.create_user(username="Satoru Gojo")
        user.set_password('sukoshirambosioka')
        user.save()

        return Wallet.objects.create(user=user, balance=balance)

    def test_biodata_creation(self):
        p = self.create_biodata()
        self.assertTrue(isinstance(p, Biodata))

    def test_wallet_creation(self):
        p = self.create_wallet()
        self.assertTrue(isinstance(p, Wallet))

    def test_biodata_name_max_length(self):
        p = self.create_biodata()
        max_length = p._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_biodata_email_max_length(self):
        p = self.create_biodata()
        max_length = p._meta.get_field('email').max_length
        self.assertEqual(max_length, 255)

    def test_biodata_gender_max_length(self):
        p = self.create_biodata()
        max_length = p._meta.get_field('gender').max_length
        self.assertEqual(max_length, 255)

    def test_biodata_phone_number_max_length(self):
        p = self.create_biodata()
        max_length = p._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 255)

    def test_edit_biodata(self):
        p = self.create_biodata()
        id = p.id

        data = {
            'name' : 'Gojo Satoru',
            'email' : 'sukoshi@rambo.sioka',
            'gender' : 'male',
            'birthday' : '1989-12-7',
            'phone_number' : '0812345678'
        }

        response = self.client.post(f'/edit-biodata/{id}', data)
        self.assertEqual(response.status_code, 200)

    def test_topup_wallet(self):
        p = self.create_wallet()
        id = p.id

        data = {
            'balance' : 1000000,
        }
        response = self.client.post(f'/topup-wallet/{id}', data)
        self.assertEqual(response.status_code, 200)

    def test_get_biodata_json(self):
        user = User.objects.create_user(username="Satoru Gojo")
        user.set_password('sukoshirambosioka')
        user.save()

        client = Client()
        client.login(username='Satoru Gojo', password='sukoshirambosioka')
        response = client.get("/get-biodata/{}/".format(user.id), follow=True)

        self.assertEqual(response.status_code, 404)

    def test_get_wallet_json(self):
        user = User.objects.create_user(username="Satoru Gojo")
        user.set_password('sukoshirambosioka')
        user.save()

        client = Client()
        client.login(username='Satoru Gojo', password='sukoshirambosioka')
        response = client.get("/get-wallet/{}/".format(user.id), follow=True)

        self.assertEqual(response.status_code, 404)
