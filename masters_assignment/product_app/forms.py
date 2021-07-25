from django import forms
from django.forms import fields, models
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["slug"]
        labels = {
            "name": "Prdouct Name"
        }