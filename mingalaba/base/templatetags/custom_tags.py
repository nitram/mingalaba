from django import template

register = template.Library()

@register.filter
def split_into_words(text):
    return text.split()