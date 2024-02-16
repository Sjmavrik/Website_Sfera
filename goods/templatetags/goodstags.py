from django import template

from goods.models import Category


register = template.Library()


@register.simple_tag()
def teg_category():
    return Category.objects.all()