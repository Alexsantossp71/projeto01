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
    regex = re.compile(r'^(?=.[a-z])(?=.[A-Z])(?=.[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'password must have at least 1 uppercase letter,'
            '1 lowercase letter, 1 number.'
            'The length at list 8 characters'),
            code='Invalid',

        )


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex. Jonh')
        add_placeholder(self.fields['last_name'], 'Ex. Doe ')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password',
        }),
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
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password',
        })

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

        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last rname',
            'email': 'E-mail',
            'password': 'Password',
        }

        help_texts = {
            'email': 'The e-mail must be valid.'
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your first name here',
            }),

        }

    def clean_password(self):
        data = self.cleaned_data.get("password")

        if 'ate' in data:
            raise forms.ValidationError(
                'Valor inválido',
                code='invalid',
                params={'pipoca': 'ate'}

            )

        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'As senhas devem ser iguais',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [password_confirmation_error],
            }
            )
