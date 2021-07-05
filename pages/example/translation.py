from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from pages.example.models import ExamplePage


@register(ExamplePage)
class ExamplePageTranslation(TranslationOptions):
    fields = ("body",)
