from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    
    # Hero section
    hero_banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Banner image (landscape)"
    )
    hero_text = models.CharField(max_length=254, null=True)

    # Welcome section
    welcome_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Welcome image (portrait)"
    )
    welcome_title = models.CharField(max_length=254, null=True, verbose_name="Welcome Title")
    welcome_paragraph = RichTextField(null=True)
    about_cta_text = models.CharField(max_length=254, null=True, verbose_name="Button Text (About Page)")

    # Menu section
    menu_cta_text = models.CharField(max_length=254, null=True, verbose_name="Button Text (Menu Page)")

    # Gallery section
    gallery_text = models.CharField(max_length=254, null=True, verbose_name="Gallery Text")
    gallery_cta_text = models.CharField(max_length=254, null=True, verbose_name="Button Text (Gallery Page)")

    # Admin panel
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_banner"),
                FieldPanel("hero_text"),
            ],
            heading="Hero Section"
        ),
        MultiFieldPanel(
            [
                FieldPanel("welcome_img"),
                FieldPanel("welcome_title"),
                FieldPanel("welcome_paragraph"),
                FieldPanel("about_cta_text"),
            ],
            heading="Welcome Section"
        ),
        MultiFieldPanel(
            [
                FieldPanel("menu_cta_text"),
            ],
            heading="Menu Section"
        ),
        MultiFieldPanel(
            [
                FieldPanel("gallery_text"),
                FieldPanel("gallery_cta_text"),
            ],
            heading="Gallery Section"
        )
    ]
    