from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from pages.about.models import AboutPage


@register(AboutPage)
class AboutPageTranslation(TranslationOptions):
    fields = ("body",)
