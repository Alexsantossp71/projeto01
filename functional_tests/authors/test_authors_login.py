from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from django.urls import reverse
import pytest

@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_with_success(self):
        #cria user
        user = User.objects.create_user(username='my_user', password='P@ssw0rd')

        #abre pagina
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # ver o formulafio de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_element_by_placeholder(form, "Type your username")        
        password_field = self.get_element_by_placeholder(form, "Type your password")        
        username_field.send_keys('my_user')
        password_field.send_keys('P@ssw0rd')
        form.submit()
        
        self.assertIn(
            f'You are loged in', 
            self.browser.find_element(By.TAG_NAME, 'body').text
            )
        
    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(
            self.live_server_url + 
            reverse('authors:login_create')
            )
        self.assertIn(
            'Not Found',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
    def test_form_login_invalid(self):
        #abre pagina de login
        self.browser.get(self.live_server_url + reverse('authors:login'))
        # tenta enviar valores vazios
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_element_by_placeholder(form, "Type your username")        
        password_field = self.get_element_by_placeholder(form, "Type your password")        
        username_field.send_keys(' ')
        password_field.send_keys(' ')        
        form.submit()

        # ve mensagem de erro na tela

        self.assertIn(
            'Invalid username or Passowrd',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_login_invalid_credentials(self):
        #abre pagina de login
        self.browser.get(self.live_server_url + reverse('authors:login'))
        # tenta enviar valores com dados não validos
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_element_by_placeholder(form, "Type your username")        
        password_field = self.get_element_by_placeholder(form, "Type your password")        
        username_field.send_keys('opaido john ')
        password_field.send_keys('P@ssw0rd')        
        form.submit()

        # ve mensagem de erro na tela

        self.assertIn(
            'Invalid credentials',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

        
