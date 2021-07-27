from django import forms
from .models import *
from .models import Category
from django.core.exceptions import ValidationError


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        product_category = forms.ModelChoiceField(queryset=Category.objects.all())
        fields = ['product_category', 'name', 'price', 'description', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SearchForm(forms.Form):
    min_price = forms.IntegerField(label="for", required=False)
    max_price = forms.IntegerField(label="to", required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Category", required=False)

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


class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
