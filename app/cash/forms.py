from django import forms
from .models import Category, Subcategory, Type, Record, Status
from django.core.exceptions import ValidationError

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        empty_label="Выберите тип",
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите категорию",
        widget=forms.Select(attrs={'class': 'form-select'})
    )



class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']  # Укажите поля, которые вы хотите редактировать
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TypesForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name',]  # Укажите поля, которые вы хотите редактировать
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RecordsForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'status', 'type', 'category', 'subcategory', 'write_comment', 'amount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'write_comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})  # Добавили поле amount
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Можно добавить динамическую выборку категорий и подкатегорий
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id).order_by('name')
            except (ValueError, TypeError):
                pass

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass

        self.fields['write_comment'].required = False


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'status', 'type', 'category', 'subcategory', 'amount', 'write_comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'write_comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is None or amount < 0:
            raise ValidationError('Сумма не может быть отрицательной!')
        return amount

