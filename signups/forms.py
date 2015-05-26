from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = [ 'last_name','first_name', 'email']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
    
        if not extension == "com":
            raise forms.ValidationError("Use a valid .COM email")
        print email
        return email