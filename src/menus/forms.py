from django import forms

from .models import Item
from restaurants.models import Restaurant
# Create your forms here

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]
    def __init__(self, user=None, *args, **kwargs):
        print(user)
        print(kwargs)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(owner=user)
