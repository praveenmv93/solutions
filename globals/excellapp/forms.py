from django import forms
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import staff, student, client


class clientForm(forms.Form):
    client_name = forms.CharField()
    client_email = forms.EmailField()
    client_phone = forms.IntegerField()
    client_password = forms.CharField()


class studentForm(forms.Form):
    stu_name = forms.CharField()
    stu_email = forms.EmailField()
    stu_phone = forms.IntegerField()
    stu_address = forms.CharField()
    stu_age = forms.IntegerField()
    stu_college = forms.CharField()
    stu_course = forms.CharField()
    stu_language = forms.CharField()
    pro_due = forms.DateField()
    stu_fee = forms.CharField()
    stu_password = forms.CharField()
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()


class staffForm(forms.Form):
    staff_name = forms.CharField()
    staff_email = forms.EmailField()
    staff_phone = forms.IntegerField()
    staff_address = forms.CharField()
    staff_job = forms.CharField()
    staff_exp = forms.CharField()
    staff_qualify = forms.CharField()
    staff_salary = forms.IntegerField()
    staff_password = forms.CharField()


class ClientSuggestionForm(forms.Form):
    suggestion = forms.CharField(max_length=100)
