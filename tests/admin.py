from django.contrib import admin
from .models import Test, TestDetails, Question ,Choices, Responses, Selcted_choices
# Register your models here.
admin.site.register(Test)
admin.site.register(TestDetails)
admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(Responses)
admin.site.register(Selcted_choices)