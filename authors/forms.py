from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'password must have at least 1 uppercase letter,'
            '1 lowercase letter, 1 number.'
            'The length at least 8 characters'
        ),
            code='Invalid',
        )


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex. Jonh')
        add_placeholder(self.fields['last_name'], 'Ex. Doe')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')

    username = forms.CharField(
        label='Username',
        help_text=(
            'Username must have letters, numbers and one of those @/./+/-/_',
            'The length should be between 4 and 150 characters'
        ),
        # 'Obrigatório. 150 caracteres ou menos. Letras, números e  @/./+/-/_ apenas.',
        error_messages={
            'required': 'Username must not be empty',
            'min_length': 'User must have at least 4 characters',
            'max_length': 'User must have less than 150 characters',
        },
        min_length=4,
        max_length=150,

    )

    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        label='First name',
    )

    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        label='Last name',
    )

    email = forms.CharField(
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='The e-mail must be valid.'
    )

    password = forms.CharField(
        required=True,
        label='Password',
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'password must have at least 1 uppercase letter,'
            '1 lowercase letter, 1 number.'
            'The length at list 8 characters'
        ),
        validators=[strong_password]
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Repeat Password'
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean_password(self):
        data = self.cleaned_data.get("password")
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and Password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [password_confirmation_error],
            }
            )
