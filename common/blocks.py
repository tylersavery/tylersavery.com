from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock


from common.enums import Alignment, Size, Aspect


class CodeSnippetBlock(blocks.StructBlock):
    language = blocks.ChoiceBlock(
        choices=[("python", "Python"), ("javascript", "Javascript"), ("css", "CSS")],
        default="python",
    )
    code = blocks.RawHTMLBlock()

    class Meta:
        icon = "code"
        template = "blocks/block_code_snippet.html"


class TextColumnBlock(blocks.StructBlock):
    body = blocks.RichTextBlock()
    width = blocks.IntegerBlock(min_value=1, max_value=12)
    offset = blocks.IntegerBlock(min_value=0, max_value=11, default=0)
    alignment = blocks.ChoiceBlock(
        choices=[
            (Alignment.LEFT.value, Alignment.LEFT.label),
            (Alignment.RIGHT.value, Alignment.RIGHT.label),
            (Alignment.CENTER.value, Alignment.CENTER.label),
        ],
        default=Alignment.LEFT,
    )


class TextColumnsBlock(blocks.StructBlock):
    columns = blocks.ListBlock(TextColumnBlock())

    class Meta:
        icon = "column"
        template = "blocks/block_text_column.html"


class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)

    page = blocks.PageChooserBlock(required=False)
    document = DocumentChooserBlock(required=False)
    external_url = blocks.URLBlock(required=False)
    button_label = blocks.CharBlock(default="Continue")

    alignment = blocks.ChoiceBlock(
        choices=[
            (Alignment.LEFT.value, Alignment.LEFT.label),
            (Alignment.RIGHT.value, Alignment.RIGHT.label),
            (Alignment.CENTER.value, Alignment.CENTER.label),
        ],
        default=Alignment.LEFT,
    )

    class Meta:
        label = "CTA"
        icon = "link"
        template = "blocks/block_cta.html"


class DividerBlock(blocks.StructBlock):

    is_full_width = blocks.BooleanBlock(default=False, required=False)

    class Meta:
        icon = "horizontalrule"
        template = "blocks/block_divider.html"


class HeadingBlock(blocks.StructBlock):
    body = blocks.TextBlock()
    alignment = blocks.ChoiceBlock(choices=Alignment.choices, default=Alignment.CENTER)
    size = blocks.ChoiceBlock(choices=Size.choices, default=Size.LARGE)

    class Meta:
        icon = "title"
        template = "blocks/block_heading.html"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)
    size = blocks.ChoiceBlock(choices=Size.choices, default=Size.LARGE)
    aspect = blocks.ChoiceBlock(choices=Aspect.choices, default=Aspect.ORIGINAL)
    is_full_width = blocks.BooleanBlock(default=False, required=False)
    enable_lightbox = blocks.BooleanBlock(default=False, required=False)
    page_link = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/block_image.html"


class GalleryImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)
    page_link = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)


class GalleryBlock(blocks.StructBlock):
    images = blocks.ListBlock(GalleryImageBlock())
    caption = blocks.TextBlock(required=False)
    size = blocks.ChoiceBlock(choices=Size.choices, default=Size.LARGE)
    aspect = blocks.ChoiceBlock(choices=Aspect.choices, default=Aspect.ORIGINAL)
    enable_lightbox = blocks.BooleanBlock(default=True, required=False)

    class Meta:
        icon = "table"
        template = "blocks/block_gallery.html"


class RichTextBlock(blocks.StructBlock):
    body = blocks.RichTextBlock()
    size = blocks.ChoiceBlock(choices=Size.choices, default=Size.MEDIUM)
    alignment = blocks.ChoiceBlock(choices=Alignment.choices, default=Alignment.LEFT)

    class Meta:
        icon = "pilcrow"
        template = "blocks/block_rich_text.html"


class SpacerBlock(blocks.StructBlock):
    size = blocks.ChoiceBlock(choices=Size.choices, default=Size.MEDIUM)

    class Meta:
        icon = "placeholder"
        template = "blocks/block_spacer.html"


class VideoBlock(blocks.StructBlock):
    embed = EmbedBlock()

    class Meta:
        icon = "media"
        template = "blocks/block_video.html"


class VideoListBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    caption = blocks.RichTextBlock(required=False)
    videos = blocks.ListBlock(VideoBlock())

    class Meta:
        icon = "media"
        template = "blocks/video_list_block.html"


DEFAULT_BLOCKS = [
    ("cta", CTABlock()),
    ("divider", DividerBlock()),
    ("gallery", GalleryBlock()),
    ("heading", HeadingBlock()),
    ("image", ImageBlock()),
    ("code_snippet", CodeSnippetBlock()),
    ("rich_text", RichTextBlock()),
    ("spacer", SpacerBlock()),
    ("text_column", TextColumnsBlock()),
    ("video", VideoBlock()),
    ("video_list", VideoListBlock()),
]
