from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from common.blocks import DEFAULT_BLOCKS


class FlexPage(Page):

    template = "pages/page_flex.html"

    body = StreamField(DEFAULT_BLOCKS, blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Flex Page"
