# Generated by Django 3.1.5 on 2021-01-25 21:51

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0059_apply_collection_ordering"),
        ("wagtailimages", "0022_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("body", wagtail.core.fields.RichTextField(blank=True)),
                ("body_en", wagtail.core.fields.RichTextField(blank=True, null=True)),
                ("body_fr", wagtail.core.fields.RichTextField(blank=True, null=True)),
                (
                    "hero_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={"verbose_name": "Home Page",},
            bases=("wagtailcore.page",),
        ),
    ]
