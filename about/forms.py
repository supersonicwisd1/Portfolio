from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', required=False)
    email = forms.EmailField(label='Your email')
    subject = forms.CharField(max_length=120)
    message = forms.CharField(widget=forms.Textarea)

