from django.forms import ModelForm
from .models import *
from django import forms


class CredentialForm(ModelForm):
    class Meta:
        model = Credential
        fields = '__all__'

        labels = {
            'name': '',
            'rollNum': '',
            'dob': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'rollNum': forms.TextInput(attrs={'class':'form-control','placeholder':'Roll number'}),
            'dob': forms.DateInput(attrs={'class':'form-control','placeholder':'Date-of-birth'}),
        }


class MarkForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

        labels = {
            'credential': '',
            'mark': '',
        }

        student_arr = {}
        saved_std = Credential.objects.all()

        print(saved_std)

        widgets = {
            #'credential': forms.TextInput(attrs={'class':'form-control','placeholder':'Roll number'}),
            'credential':forms.Select(choices=student_arr),
            # 'credential': forms.ModelChoiceField(queryset=Report.objects.all()),
            'mark': forms.TextInput(attrs={'class':'form-control','placeholder':'Mark'}),
        }