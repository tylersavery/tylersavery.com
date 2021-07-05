import locale
from project.settings.constants.env import ENV

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGES = [("en", "English"), ("fr", "Français")]
LANGUAGE_CODES = [language[0] for language in LANGUAGES]
LANGUAGE_CODE = ENV.str("LANGUAGE_CODE", default="en")
TIME_ZONE = ENV.str("TIME_ZONE", default="UTC")
USE_I18N = False
USE_L10N = False
USE_TZ = True
