from django import template

from goods.models import Category
from main.models import Navigate


register = template.Library()


@register.simple_tag()
def teg_category():
    return Category.objects.all()
