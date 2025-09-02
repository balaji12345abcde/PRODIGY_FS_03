from django import forms
from .models import Product, Review, SupportQuery

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','category','image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name','rating','comment']

class SupportForm(forms.ModelForm):
    class Meta:
        model = SupportQuery
        fields = ['name','email','message']
