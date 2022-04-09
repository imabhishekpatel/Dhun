from django import forms
from django.db.models import fields
from .models import User
from django.contrib.auth.hashers import check_password

class Signupform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    retype_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:    
        model=User
        fields=['name','email','username']
    def clean(self):
        super().clean()
        p=self.cleaned_data.get('password')
        p1=self.cleaned_data.get('retype_password')
        if p!=p1:
            raise forms.ValidationError("Both password did not match")

class Signinform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data.get('username')
        p=self.cleaned_data.get('password')
        try:
            us=User.objects.get(username=u)
        except:
            raise forms.ValidationError("user doesnot exits")
        else:
            if not check_password(p,us.password):
                raise forms.ValidationError("password doesnot match")


