import django.conf.global_settings as DEFAULT_SETTINGS

SECRET_KEY = 'test-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'filechooser',
)

FILECHOOSER = {
    'jquery_js_url': 'some-cdn-url',
    'datatable_css_url': 'some-other-cdn-url'
}

STATIC_URL = '/static/'

MIDDLEWARE_CLASSES = DEFAULT_SETTINGS.MIDDLEWARE_CLASSES
