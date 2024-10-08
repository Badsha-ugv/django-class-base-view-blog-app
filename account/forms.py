from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 



class UserCreationForm(UserCreationForm):

    class Meta:
        model = User 
        fields = ['username','email','password1','password2']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'usable_password' in self.fields:
            del self.fields['usable_password']
            
        for field in self.fields.values():
            field.help_text = ''