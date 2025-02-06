from django import forms
from .models import Category, Subcategory, Type

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']

    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        empty_label="Выберите тип",
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name']

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите категорию",
        widget=forms.Select(attrs={'class': 'form-select'})
    )