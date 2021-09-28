from django import forms
from .models import Signup, MailMessage


class SignMeUp(forms.ModelForm):
    
    class Meta:
        model = Signup
        fields = ('email', )
        

class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'