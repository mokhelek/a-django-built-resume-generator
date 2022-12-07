from django import template
register = template.Library()


def modulo(num,val):
    return num % val
    

register.filter("modulo",modulo)