from django import forms
from django.db.models import fields
from django.utils.regex_helper import Choice
from .models import TestDetails, Test, Responses

class CreateTestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
    class Meta:
        model = Test
        fields = ('test_title',)
        required=('test_title',)

class TestDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
    
    class Meta:
        model = TestDetails
        fields = ('test_total_time','no_of_questions', 'marks',)
        required=('test_total_time','no_of_questions', 'marks',)
        
Choices=(('1','1'),('2','2'),('3','3'),('4','4'))
class AddQuestionForm(forms.Form):
    question=forms.CharField(label='Q. ',max_length=1000, required=True)
    choice1=forms.CharField(label='1. ',max_length=500, required=True)
    choice2=forms.CharField(label='2. ',max_length=500, required=True)
    choice3=forms.CharField(label='3. ',max_length=500, required=True)
    choice4=forms.CharField(label='4. ',max_length=500, required=True)
    correct=forms.ChoiceField(label='Correct', choices=Choices, required=True)
    
class ResponseDetailsForm(forms.ModelForm):
    
    class Meta:
        model=Responses
        
        fields=('student_name', 'email', 'roll_no')
        required=('student_name', 'email', 'roll_no')
    
    
