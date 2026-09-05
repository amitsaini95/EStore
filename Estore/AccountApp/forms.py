from django import forms
from .models import Account
from django.contrib.auth.forms import AuthenticationForm
class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Confirm Password'}))
    class Meta:
        model=Account
        fields=('username','email','phoneNumber','password','confirm_password')

    def __init__(self,*args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        
        for field,field_name in self.fields.items():
            field_name.widget.attrs['placeholder']=f'Enter the {field}'
            field_name.widget.attrs['class'] = 'form-control'
    def clean(self):
        cleaned_data= super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password !=confirm_password:
            raise forms.ValidationError("password does not match")
        return cleaned_data
class LoginForm(forms.Form):
    email=forms.CharField(label="email",max_length=200,widget=forms.EmailInput())
    password=forms.CharField(label='password',max_length=200,widget=forms.PasswordInput())
    
    def __init__(self,*args, **kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)
            
        for field,field_name in self.fields.items():
            field_name.widget.attrs['placeholder']=f'Enter the {field}'
            field_name.widget.attrs['class'] = 'form-control'