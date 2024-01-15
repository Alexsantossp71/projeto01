from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class AuthorsBaseTest(StaticLiveServerTestCase):
    def setUp(self)->None:
        self.browser = make_chrome_browser()
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
    
    def sleep(self, qtd=10):
        return sleep(qtd)
    
    def get_element_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
                By.XPATH, f'//input[@placeholder="{placeholder}"]'
            )
    
    def  form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register')
        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('dummy@email.com')
            
        callback(form)
        return form