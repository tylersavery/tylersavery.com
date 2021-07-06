# Generated by Django 3.1.5 on 2021-07-06 16:23

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0017_auto_20210706_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(required=False)), ('button_label', wagtail.core.blocks.CharBlock(default='Continue')), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')]))])), ('divider', wagtail.core.blocks.StructBlock([('is_full_width', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('gallery', wagtail.core.blocks.StructBlock([('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))), ('caption', wagtail.core.blocks.TextBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('aspect', wagtail.core.blocks.ChoiceBlock(choices=[('original', 'Original'), ('square', 'Square'), ('portrait', 'Portrait'), ('landscape', 'Landscape')])), ('enable_lightbox', wagtail.core.blocks.BooleanBlock(default=True, required=False))])), ('heading', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.TextBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('aspect', wagtail.core.blocks.ChoiceBlock(choices=[('original', 'Original'), ('square', 'Square'), ('portrait', 'Portrait'), ('landscape', 'Landscape')])), ('is_full_width', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('enable_lightbox', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('page_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))])), ('code_snippet', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('python', 'Python'), ('javascript', 'Javascript'), ('css', 'CSS')])), ('code', wagtail.core.blocks.RawHTMLBlock())])), ('rich_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))])), ('spacer', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]))])), ('video', wagtail.core.blocks.StructBlock([('embed', wagtail.embeds.blocks.EmbedBlock())])), ('video_list', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('videos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('embed', wagtail.embeds.blocks.EmbedBlock())])))]))], blank=True, null=True),
        ),
    ]
