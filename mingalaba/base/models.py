from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from wagtail.admin.panels import FieldPanel, FieldRowPanel
from wagtail.models import (
    DraftStateMixin,
    LockableMixin,
    Page,
    RevisionMixin,
)
from wagtail.snippets.models import register_snippet


class Logo(DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
    name = models.CharField(blank=True, max_length=254, unique=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Logo image (<sizing>)"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.name
    

class Phone(DraftStateMixin, RevisionMixin, models.Model):
    phone = PhoneNumberField(region="US")

    panels = [
        FieldPanel("phone")
    ]

    def __str__(self):
        return self.phone.as_national


class Address(DraftStateMixin, RevisionMixin, models.Model):
    street1 = models.CharField(max_length=254, null=True)
    street2 = models.CharField(blank=True, max_length=254, null=True)
    apartment = models.CharField(blank=True, max_length=254, null=True, verbose_name="Apartment / Building")
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    city = models.CharField(max_length=254, null=True)
    zipcode = models.CharField(max_length=5, null=True)

    panels = [
        FieldPanel("street1"),
        FieldPanel("street2"),
        FieldPanel("apartment"),
        FieldPanel("state"),
        FieldPanel("city"),
        FieldPanel("country"),
        FieldPanel("zipcode"),
    ]

    class Meta:
        verbose_name="Addresses"
        verbose_name_plural="Addresses"

    def __str__(self):
        return f"{self.street1}, {self.city}"


class Hours(DraftStateMixin, RevisionMixin, models.Model):
    option = models.CharField(blank=True, max_length=254)
    time = models.CharField(max_length=254, null=True)

    panels = [
        FieldPanel("option"),
        FieldPanel("time"),
    ]

    class Meta:
        verbose_name="Hours"
        verbose_name_plural="Hours"

    def __str__(self):
        return f"{self.option} | {self.time} "
    

class Socials(DraftStateMixin, RevisionMixin, models.Model):
    type = models.CharField(max_length=254, null=True)
    link = models.URLField(null=True)

    panels = [
        FieldPanel("type"),
        FieldPanel("link"),
    ]

    class Meta:
        verbose_name="Socials"
        verbose_name_plural="Socials"

    def __str__(self):
        return self.type


class AboutPage(Page):
    pass


class GalleryPage(Page):

    # Hero section
    gallery_banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Banner image (landscape)"
    )

    # Admin panel
    content_panels = Page.content_panels + [
        FieldPanel("gallery_banner")
    ]


class ContactPage(Page):
    pass