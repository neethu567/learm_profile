from django import forms
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class Resetform(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    # def is_valid(self):
    #     self.cleaned_data
    #     return True
from django.core.exceptions import ValidationError

class ProfileForm(forms.Form):
    first_name=forms.CharField(max_length=200,initial = "first name")
    last_name=forms.CharField(max_length=200 ,initial = "last name")
    # profile_pic = forms.FileField(max_length=200,allow_empty_file=True)
    # birth_date=forms.DateField()
    mobile_number=forms.IntegerField(initial = 242342342)
    address=forms.CharField(max_length=500 ,initial = "your address")
    country=forms.CharField(max_length=200 ,initial = "india")
    #
    # class Meta:
    #     model=Profile
    #     # fields=('first_name','last_name','mobile_number','address','country',)
    #     fields=('mobile_number','address','country',)
    #     # fields=('first_name','last_name','profile_pic','birth_date','mobile_number','address','country',)

    #
    # def clean(self):
    #     super(ProfileForm,self).clean()
    #     country=self.cleaned_data.get('country')
    #     if "india" not in country:
    #         raise ValidationError("Indian citizens ae only allowed")
    #     return country