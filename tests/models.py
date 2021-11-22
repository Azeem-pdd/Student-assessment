from django.db import models
from django.db.models.deletion import DO_NOTHING
from accounts.models import User
# Create your models here.
class Test(models.Model):
    test_title=models.CharField(verbose_name='Test Title',max_length=100, blank=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    identifier=models.CharField(max_length=2000, null=True, blank=True)
    accept=models.BooleanField(default=False)
    def __str__(self):
        return self.test_title
    
class TestDetails(models.Model):
    user=models.ForeignKey(User,verbose_name='test created by', on_delete=models.CASCADE)
    test=models.ForeignKey(Test, on_delete=models.CASCADE)
    test_total_time=models.PositiveIntegerField(null=True, blank=True)
    no_of_questions=models.PositiveIntegerField(null=True, blank=True)
    marks=models.PositiveIntegerField(verbose_name='marks for each Q. ',null=True, blank=True, default=1)
    
    def __str__(self):
        return self.test.test_title
    
    
class Question(models.Model):
    question=models.CharField(verbose_name="Q. ", max_length=1000, blank=True, null=True)
    test=models.ForeignKey(Test, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question
    
    
class Choices(models.Model):
    choice=models.CharField(max_length=500, blank=True, null=True)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    correct=models.BooleanField(default=False)
    
    def __str__(self):
        return self.choice
    
    
class Responses(models.Model):
    test=models.ForeignKey(Test, on_delete=models.CASCADE)
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    total_no_of_questions=models.PositiveIntegerField(null=True, blank=True)
    correct_questions=models.PositiveIntegerField(blank=True, null=True)
    obtained_marks=models.PositiveIntegerField(blank=True, null=True)
    student_name=models.CharField(max_length=150, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    roll_no=models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.student_name
class Selcted_choices(models.Model):
    res_obj=models.ForeignKey(Responses, on_delete=models.CASCADE)
    c_id=models.PositiveIntegerField(null=True, blank=True)