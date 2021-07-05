from .i18n import LANGUAGES

# Wagtail
# https://docs.wagtail.io/

WAGTAIL_APPEND_SLASH = True
WAGTAIL_CONTENT_LANGUAGES = LANGUAGES
WAGTAIL_ENABLE_UPDATE_CHECK = False
WAGTAIL_SITE_NAME = "Boilerplate"

# wagtail-modeltranslation
# https://wagtail-modeltranslation-docs.readthedocs.io

WAGTAILMODELTRANSLATION_LOCALE_PICKER = True

# wagtailmenus
# https://wagtailmenus.readthedocs.io/

WAGTAILMENUS_FLAT_MENUS_EDITABLE_IN_WAGTAILADMIN = False

# django-taggit
# https://django-taggit.readthedocs.io/

TAGGIT_CASE_INSENSITIVE = True
