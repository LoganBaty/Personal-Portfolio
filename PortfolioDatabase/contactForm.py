from django import forms
from .models import Contact, Portfolio

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Your name", max_length=100)
    email = forms.CharField(required=True, label="Your email", max_length=100)
    message = forms.CharField(required=True, label="Your message", max_length=500)

    def log_data(self):
        print(self.cleaned_data.get("name"))
        print(self.cleaned_data.get("email"))
        print(self.cleaned_data.get("message"))

class ContactModelForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','message']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['project_title', 'project_desc', 'project_image', 'project_paragraph']