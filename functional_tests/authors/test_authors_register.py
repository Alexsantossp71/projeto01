from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import pytest

@pytest.mark.functional_test
class AuthorsRegisterTest(AuthorsBaseTest):

        
        def fill_form_dummy_data(self, form):
            fields = form.find_elements(By.TAG_NAME, 'input')

            for field in fields:
                if field.is_displayed():
                    field.send_keys(' ' * 20)

        def get_form(self):
            return self.browser.find_element(
                  By.XPATH, 
                  '/html/body/main/div/div[2]/form'
                  )             
        
        def test_empty_first_name_error_message(self):
            def callback(form):
                first_name_field =  self.get_element_by_placeholder(form, "Ex. Jonh")
                first_name_field.send_keys(' ')
                first_name_field.send_keys(Keys.ENTER)
                form = self.get_form()
                self.assertIn('Write your last name', form.text)
            self.form_field_test_with_callback(callback)

        def test_empty_last_name_error_message(self):
            def callback(form):
                last_name_field =  self.get_element_by_placeholder(form, "Ex. Doe")
                last_name_field.send_keys(' ')
                last_name_field.send_keys(Keys.ENTER)
                form = self.get_form()
                self.assertIn('Write your last name', form.text)
            self.form_field_test_with_callback(callback)

        def test_empty_username_error_message(self):
            def callback(form):
                username_field =  self.get_element_by_placeholder(form, "Your username")
                username_field.send_keys(' ')
                username_field.send_keys(Keys.ENTER)
                form = self.get_form()
                self.assertIn('Username must not be empty', form.text)
            self.form_field_test_with_callback(callback) 

        def test_empty_email_error_message(self):
            def callback(form):   
                email_field =  self.get_element_by_placeholder(form, "Your e-mail")
                #email_field.send_keys(' ')
                form.find_element(By.NAME, 'email').send_keys('\uE003' * 40)
                form.find_element(By.NAME, 'email').send_keys(' ')
                email_field.send_keys(Keys.ENTER)
                form = self.get_form()

                self.sleep(5)
                self.assertIn('E-mail is required', form.text)
            self.form_field_test_with_callback(callback) 

        def test_empty_password_error_message(self):
            def callback(form):
                password_field =  self.get_element_by_placeholder(form, "Type your password")
                password_field.send_keys(' ')
                password_field.send_keys(Keys.ENTER)
                form = self.get_form()
                self.assertIn('Password must not be empty', form.text)
            self.form_field_test_with_callback(callback) 

        def test_empty_password2_error_message(self):
            def callback(form):
                password2_field =  self.get_element_by_placeholder(form, "Repeat your password")
                password2_field.send_keys(' ')
                password2_field.send_keys(Keys.ENTER)
                form = self.get_form()
                self.assertIn('Please, repeat your password', form.text)
            self.form_field_test_with_callback(callback)

        def test_invalid_email_error_message(self):
            def callback(form):   
                email_field =  self.get_element_by_placeholder(form, "Your e-mail")
                form.find_element(By.NAME, 'email').send_keys('\uE003' * 40)
                form.find_element(By.NAME, 'email').send_keys('a@a')
                email_field.send_keys(Keys.ENTER)
                form = self.get_form()
                self.assertIn('Informe um endereço de email válido.', form.text)
            self.form_field_test_with_callback(callback) 

        def test_password_do_not_match(self):
            def callback(form):
                password1 =  self.get_element_by_placeholder(form, "Type your password")
                password2 =  self.get_element_by_placeholder(form, "Repeat your password")               
                password1.send_keys('P@ssw0rd')
                password2.send_keys('P@ssw0rd_Different')
                password2.send_keys(Keys.ENTER)
                form = self.get_form()
                self.assertIn('Password and Password2 must be equal', form.text)
            self.form_field_test_with_callback(callback)
        
        def test_user_valid_data_register_successfully(self):
            self.browser.get(self.live_server_url + '/authors/register')
            form = self.get_form()

            self.get_element_by_placeholder(form, "Ex. Jonh").send_keys('Jonh')
            self.get_element_by_placeholder(form, "Ex. Doe").send_keys('Doe')
            self.get_element_by_placeholder(form, "Your username").send_keys('username')
            self.get_element_by_placeholder(form, "Your e-mail").send_keys('jd@jd.net')
            self.get_element_by_placeholder(form, "Type your password").send_keys('P@ssw0rd')
            self.get_element_by_placeholder(form, "Repeat your password") .send_keys('P@ssw0rd')
          
            form.submit()
            self.sleep(5)
            self.assertIn(
                'Usuário criado com sucesso', 
                self.browser.find_element(By.TAG_NAME, 'body').text
                )





