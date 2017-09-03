from django import forms

from .models import Restaurant
from .validators import validate_category
# Code here

'''
class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "React":
            raise forms.ValidationError("Not a valid name!")
        return name
'''

class RestaurantCreateForm(forms.ModelForm):
    # email = forms.EmailField()
    # category = forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'location',
            'category',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name.lower() == 'create':
            raise forms.ValidationError("{} is a not valid name!".format(name))
        return name

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if ".edu" in email:
    #         raise forms.ValidationError("We do not accept .edu emails")
    #     return email
