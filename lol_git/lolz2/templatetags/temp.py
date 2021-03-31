from django import template
register = template.Library()


@register.filter(name="low")
def low(self):
    return self.lower()
