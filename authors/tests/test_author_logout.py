from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthorLogoutTest(TestCase):
    def test_user_tries_to_logout_using_get_metod(self):
        #cria user
        user = User.objects.create_user(username='my_user', password='P@ssw0rd')
        self.client.login(username='my_user', password='P@ssw0rd')

        response = self.client.get(
            reverse('authors:logout'),
            follow=True,
            )

        self.assertIn(
            'Invalid logout request',
            response.content.decode('utf-8'),
            )

    def test_user_tries_to_logout_another_user(self):
        #cria user
        user = User.objects.create_user(username='my_user', password='P@ssw0rd')
        self.client.login(username='my_user', password='P@ssw0rd')

        response = self.client.post(
            reverse('authors:logout'),
            data={
                'username':'another_user'
            },
            follow=True,
            )

        self.assertIn(
            'Invalid logout user',
            response.content.decode('utf-8'),
            )
        
    def test_user_can_logout_successufuly(self):
        #cria user
        user = User.objects.create_user(username='my_user', password='P@ssw0rd')
        self.client.login(username='my_user', password='P@ssw0rd')

        response = self.client.post(
            reverse('authors:logout'),
            data={
                'username':'my_user'
            },
            follow=True,
            )

        self.assertIn(
            'Loged out successfully',
            response.content.decode('utf-8'),
            )
