# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

import os

from project.settings.enviroment import BASE_DIR


STATIC_URL = '/static/'
STATICFILES_DIRS = [  
    os.path.join(BASE_DIR / 'base_static'),
]
STATIC_ROOT = os.path.join(BASE_DIR / 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')