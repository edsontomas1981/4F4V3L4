from django import forms

class RecoveryForm(forms.Form):
    email= forms.CharField(required=True,widget=forms.EmailInput(attrs={
    'class':'form-control'}))

class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':
'form-control'}))
    