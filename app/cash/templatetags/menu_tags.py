from django import template
from django.utils import timezone
import datetime
from cash.models import Category, Subcategory, Record


register = template.Library()


@register.simple_tag()
def get_all_Category(user):
    return Category.objects.filter(user=user)


@register.simple_tag()
def get_all_Subcategory(user):
    return Category.objects.filter(user=user)