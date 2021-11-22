from django import template
from django.http import request
import clipboard as c
from accounts.models import User
from ..models import Test
register = template.Library()
from ..models import Choices
@register.filter(name='fetch_choices')
def fetch_choices(q):
    return Choices.objects.filter(question=q)
@register.filter(name='check_test')
def check_test(test):
    if Test.objects.get(id=test).accept==True:
        return True
    else:
        return False

@register.filter(name='check_selection')
def check_selection(id, ids):
    if id in ids:
        return True
    else:
        return False
@register.filter(name='check_correctness')
def check_correctness(id):
    if Choices.objects.get(id=id).correct:
        return True
    else:
        return False