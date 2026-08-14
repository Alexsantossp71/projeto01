# Build paths inside the project like this: BASE_DIR / 'subdir'.
import os
from pathlib import Path

from utils.enviroment import get_env_variable, parse_comma_sep_str_to_list


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'INSECURE')  # noqa: E501

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = parse_comma_sep_str_to_list(
    get_env_variable('ALLOWED_HOSTS'),
)

# Application definition

CRSF_TRUSTED_ORIGINS: list[str] = parse_comma_sep_str_to_list(
    get_env_variable('CRSF_TRUSTED_ORIGINS'),
)

ROOT_URLCONF = 'project.urls'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'