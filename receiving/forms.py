from django import forms
from .models import Product, Inventory


class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ("created_at", "updated_at", "deleted_at", "id", "signature")


class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ("created_at", "updated_at", "deleted_at", "id", "signature")


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "deleted_at", "id")


class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "deleted_at", "id")