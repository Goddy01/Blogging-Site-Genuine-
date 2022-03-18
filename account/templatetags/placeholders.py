from django.template import Library

register = Library()

def placeholder(value, token):
	value.field.widget.attrs["placeholder"] = token.title()
	return value

register.filter(placeholder)