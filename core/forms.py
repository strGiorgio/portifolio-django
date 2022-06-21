from pyexpat import model
from django  import forms

from .models import UsersMessages


class UsersMessagesForm(forms.ModelForm):
    class Meta:
        model = UsersMessages
        fields = ['name', 'email', 'message']

