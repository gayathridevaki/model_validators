from django.db import models
from django import forms
from django.core import validators


# Create your models here.
def validate_for_a(data):
    if data.lower().startswith('d'):
        raise forms.ValidationError('cannot startwith d')
    
class Student(models.Model):
    sname=models.CharField(max_length=100,validators=[validate_for_a])
    sage=models.IntegerField()
    smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def __str__(self):
        return self.sname
    
    