from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting(icon="doc-full")
class LegalSettings(BaseSetting):
    copyright = models.TextField(blank=True)

    panels = [
        FieldPanel("copyright"),
    ]

    class Meta:
        verbose_name = "Legal"


@register_setting(icon="link")
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, help_text="Twitter URL")
    instagram = models.URLField(blank=True, help_text="Instagram URL")
    youtube = models.URLField(blank=True, help_text="YouTube Channel URL")
    linkedin = models.URLField(blank=True, help_text="LinkedIn URL")
    github = models.URLField(blank=True, help_text="Github URL")

    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("instagram"),
        FieldPanel("youtube"),
        FieldPanel("linkedin"),
        FieldPanel("github"),
    ]

    class Meta:
        verbose_name = "Social Media"
