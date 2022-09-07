from socket import fromshare
from django import forms
from .models import Student_table

class Student_form(forms.ModelForm):
    class Meta:
        model=Student_table
        fields="__all__"
        labels = {"first_name": "Adınız", "last_name":"Soyadınız", "number":"Numaranız"}