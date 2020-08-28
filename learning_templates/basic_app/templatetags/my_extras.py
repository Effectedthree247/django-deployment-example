from django import template

register = template.Library()

@register.filter(name='cutr')
def cutr(value,arg):
    return value.replace(arg,"")


# register.filter('cutr',cutr)
