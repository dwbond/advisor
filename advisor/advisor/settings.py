"""
Django settings for advisor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9!1f(9=vz_e_*_l88(!_7_xag@1+yadf3ac*a-h297ij@@dhw7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    'static',
)

STATICFILE_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (
    'templates',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'trajectories',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'advisor.urls'

WSGI_APPLICATION = 'advisor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ordering of apps in admin interface
# https://djangosnippets.org/snippets/1939/
# ADMIN_REORDER = (
# )

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

##### LDAP #####

import ldap
# Baseline configuration

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
'django_auth_ldap.backend.LDAPBackend',
'django.contrib.auth.backends.ModelBackend',
)

# GMU LDAP database. This is also accessible at newldap.gmu.edu
AUTH_LDAP_SERVER_URI = "ldaps://directory.gmu.edu:636"
AUTH_LDAP_BIND_DN = "ou=people,o=gmu.edu"

# Since we authenticate by logging into the LDAP server, you need to
# bind to the LDAP server as the authenticating user.
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True

# This sticks the "user" plug into the hole in the DN string.
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=people,o=gmu.edu"

# Basically this is required to ignore the self-signed GMU cert.
AUTH_LDAP_GLOBAL_OPTIONS = {
ldap.OPT_X_TLS : ldap.OPT_X_TLS_DEMAND,
ldap.OPT_X_TLS_REQUIRE_CERT : ldap.OPT_X_TLS_NEVER,
}

# Populate the Django User model from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
"first_name": "givenName",
"last_name": "sn",
"email": "mail"
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True
