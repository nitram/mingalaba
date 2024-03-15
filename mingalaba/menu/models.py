from django.db import models
from django import forms


# Create your models here.
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import (
    DraftStateMixin,
    Orderable,
    Page,
    RevisionMixin,
)
from wagtail.snippets.models import register_snippet
from wagtail.search import index


class MenuPage(Page):
    pass


class Category(index.Indexed, RevisionMixin, models.Model):
    name = models.CharField(max_length=254, null=True)
    category_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Category image (landscape)"
    )

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Food(index.Indexed, RevisionMixin, models.Model):
    name = models.CharField(max_length=254, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    note = models.CharField(blank=True, max_length=254)
    description = RichTextField(blank=True)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=5)

    panels = [
        FieldPanel("name"),
        FieldPanel("category"),
        FieldPanel("note"),
        FieldPanel("description"),
        FieldPanel("price"),
    ]

    search_fields = [
        index.SearchField("name"),
        index.AutocompleteField("name"),
        index.FilterField("category"),
    ]

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"