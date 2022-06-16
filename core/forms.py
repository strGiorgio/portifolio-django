from unicodedata import name
from django  import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=64)
    email = forms.EmailField(label='Email', max_length=128)
    message = forms.CharField(label='Message', widget=forms.Textarea())