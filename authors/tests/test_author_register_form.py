from unittest import TestCase
from django.test import TestCase as DjangoTestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('first_name', 'Ex. Jonh'),
        ('last_name', 'Ex. Doe'),
        ('username', 'Your username'),
        ('email', 'Your e-mail'),
        ('password', 'Type your password'),
        ('password2', 'Repeat your password'),
    ])
    def test_text_fields_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        # ('username', 'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'),
        ('email', 'The e-mail must be valid.'),
        ('username', (
            'Username must have letters, numbers and one of those @/./+/-/_',
            'The length should be between 4 and 150 characters'
        ),),
        ('password', (
            'password must have at least 1 uppercase letter,'
            '1 lowercase letter, 1 number.'
            'The length at list 8 characters'
        ),),
    ])
    def test_fields_help_text_is_correct(self, field, needed):
        form = RegisterForm()
        current_helptext = form[field].field.help_text
        self.assertEqual(current_helptext, needed)

    @parameterized.expand([
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
        ('username', 'Username'),
        ('email', 'E-mail'),
        ('password', 'Password'),
        ('password2', 'Repeat Password'),
    ])
    def test_fields_label_is_correct(self, field, needed):
        form = RegisterForm()
        current_label = form[field].field.label
        self.assertEqual(current_label, needed)


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@email.com',
            'password': 'Str0ngP@ssword1',
            'password2': 'Str0ngP@ssword1',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'Username must not be empty'),
        ('first_name', 'Write your first name'),
        ('last_name', 'Write your last name'),
        ('email', 'E-mail is required'),
        ('password', 'Password must not be empty'),
        ('password2', 'Please repeat your password'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))

    def test_username_field_min_lenght_should_be_4(self):
        self.form_data['username'] = 'joa'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'User must have at least 4 characters'
        # self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_username_field_max_lenght_should_be_150(self):
        self.form_data['username'] = 'A' * 151
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'User must have less than 150 characters'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_password_field_have_lower_upper_case_letters_and_numbers(self):
        self.form_data['password'] = 'abc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = (
            'password must have at least 1 uppercase letter,'
            '1 lowercase letter, 1 number.'
            'The length at least 8 characters'
        )
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('password'))

        self.form_data['password'] = '1@Aabc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.content.decode('utf-8'))
        # self.assertIn(msg, response.context['form'].errors.get('password'))

    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '1@Aabc123'
        self.form_data['password2'] = '1@Aabc1234'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = (
            'Password and Password2 must be equal'
        )
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('password'))

        self.form_data['password'] = '1@Aabc123'
        self.form_data['password2'] = '1@Aabc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.content.decode('utf-8'))
        # self.assertIn(msg, response.context['form'].errors.get('password'))
