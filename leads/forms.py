from django import forms
from .models import Lead
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = {
            "name",
            "sourname",
            'age',
            'agent'
        }

class LeadForm(forms.Form):
    name = forms.CharField(max_length=20)
    sourname = forms.CharField(max_length=25)
    age = forms.IntegerField(min_value=0)

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}