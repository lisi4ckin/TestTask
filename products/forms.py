from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    min_price = forms.IntegerField(label="for", required=False)
    max_price = forms.IntegerField(label="to", required=False)
    category = forms.CharField(label="Category", required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['min_price'].initial = 1
        self.fields['max_price'].initial = 10000

    def clean_max_price(self):
        if not self.cleaned_data['max_price']:
            return 10000
        return self.cleaned_data['max_price']

    def clean_min_price(self):
        if self.cleaned_data['min_price'] != 0:
            return 0
        return self.cleaned_data['min_price']