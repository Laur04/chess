from django import forms

class StarterForm(forms.Form):
    METHOD_OPTIONS = (("", "Please select one"), ("0", "Harris Corner Detection"))

    image = forms.ImageField(required=True)
    method = forms.ChoiceField(choices=METHOD_OPTIONS, required=True)
    custom_name = forms.CharField(max_length=50, required=False, label="Name (optional):")
