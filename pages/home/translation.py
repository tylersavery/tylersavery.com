from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from pages.home.models import HomePage


@register(HomePage)
class HomePageTranslation(TranslationOptions):
    fields = ("body",)
