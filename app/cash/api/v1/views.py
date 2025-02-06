from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from cash.models import *
from cash.forms import (
    SubcategoryForm,
    CategoryForm,
    TypeForm,
)

# Create your views here.

@login_required
def home(request):
    return render(request, 'cash/index.html')

def create_subcategory(request):
    if request.method == 'POST':
        subcategory_form = SubcategoryForm(request.POST)
        if subcategory_form.is_valid():
            subcategory_form.save()
            return redirect('subcategory_list')  # Перенаправление на список подкатегорий
    else:
        subcategory_form = SubcategoryForm()

    category_form = CategoryForm()  # Форма для добавления категории
    type_form = TypeForm()  # Форма для добавления типа

    return render(request, 'cash/create_subcategory.html', {
        'subcategory_form': subcategory_form,
        'category_form': category_form,
        'type_form': type_form
    })


def create_type(request):
    if request.method == 'POST':
        type_form = TypeForm(request.POST)
        if type_form.is_valid():
            type = type_form.save()
            return JsonResponse({
                'success': True,
                'type': type.name,  # Имя категории
                'type_id': type.id  # ID категории
            })
    else:
        type_form = TypeForm()
    return JsonResponse({'success': False})


def create_category(request):
    try:
        if request.method == 'POST':
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category = category_form.save()  # Сохраняем категорию
                print(f"Категория создана: {category.name} (ID: {category.id})")  # Выводим имя и ID категории
                return JsonResponse({
                    'success': True,
                    'category': category.name,  # Имя категории
                    'category_id': category.id  # ID категории
                })
            else:
                # Если форма не прошла валидацию, выводим ошибки формы
                print(f"Ошибка валидации формы: {category_form.errors}")
                raise ValueError("Форма не прошла валидацию")
        else:
            category_form = CategoryForm()

        return JsonResponse({'success': False, 'message': 'Ошибка при обработке запроса'})

    except ValueError as e:
        print(f"Ошибка: {e}")  # Логируем ошибку ValueError
        return JsonResponse({'success': False, 'message': str(e)})

    except Exception as e:
        print(f"Необработанная ошибка: {e}")  # Логируем все другие исключения
        return JsonResponse({'success': False, 'message': 'Произошла непредвиденная ошибка'})