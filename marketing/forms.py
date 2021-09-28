from django import forms
from .models import Signup, MailMessage
from tinymce.widgets import TinyMCE

class SignMeUp(forms.ModelForm):
    
    class Meta:
        model = Signup
        fields = ('email', )


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False        

class MailMessageForm(forms.ModelForm):
    message = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    class Meta:
        model = MailMessage
        fields = ('title', 'message')