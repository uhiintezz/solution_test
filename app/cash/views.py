from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages

from .models import *
from .forms import (
    SubcategoryForm,
    CategoryForm,
    TypeForm,
    RecordsForm,
    RecordForm,
    StatusForm,
    TypesForm,
    SubcategorysForm
)

# Create your views here.

@login_required
def home(request):
    return render(request, 'cash/index.html')

def create_subcategory(request):
    if request.method == 'POST':
        subcategory_form = SubcategoryForm(request.POST)
        if subcategory_form.is_valid():
            subcategory = subcategory_form.save(commit=False)  # Не сохраняем объект сразу
            subcategory.user = request.user  # Привязываем текущего пользователя
            subcategory.save()
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

def create_categories(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category = category_form.save(commit=False)  # Не сохраняем объект сразу
            category.user = request.user  # Привязываем текущего пользователя
            category.save()

            return redirect('category_list')
    else:
        category_form = CategoryForm()

    type_form = TypeForm()

    return render(request, 'cash/create_category.html', {
        'category_form': category_form,
        'type_form': type_form
    })


def create_type(request):
    if request.method == 'POST':
        type_form = TypeForm(request.POST)
        if type_form.is_valid():
            type = type_form.save(commit=False)
            type.user = request.user
            type.save()
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
                category = category_form.save(commit=False)  # Сохраняем категорию
                category.user = request.user
                category.save()
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




def create_record(request):
    if request.method == "POST":
        form = RecordsForm(request.POST)
        if form.is_valid():
            record_instance = form.save(commit=False)
            record_instance.user = request.user
            record_instance.save()
            return JsonResponse({"success": True, "message": "Запись успешно создана!"})
        return JsonResponse({"success": False, "errors": form.errors})

    form = RecordsForm()
    return render(request, "cash/create_record.html", {"form": form})

def get_categories(request):
    # Получаем id типа из GET-параметров
    type_id = request.GET.get("type_id")
    # Фильтруем категории по типу и пользователю
    categories = Category.objects.filter(type_id=type_id, user=request.user).values("id", "name")
    return JsonResponse(list(categories), safe=False)

def get_subcategories(request):
    # Получаем id категории из GET-параметров
    category_id = request.GET.get("category_id")
    # Фильтруем подкатегории по категории и пользователю
    subcategories = Subcategory.objects.filter(category_id=category_id, category__user=request.user).values("id", "name")
    return JsonResponse(list(subcategories), safe=False)


class StatusListView(ListView):
    model = Status
    template_name = 'cash/status_list.html'  # Шаблон для отображения списка статусов
    context_object_name = 'statuses'

    def get_queryset(self):
        # Фильтруем статусы, чтобы возвращать только те, которые принадлежат текущему пользователю
        return Status.objects.filter(user=self.request.user)

class StatusCreateView(CreateView):
    model = Status
    fields = ['name', ]  # Укажите поля, которые будут в форме
    template_name = 'cash/status_add.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        # Присваиваем текущего пользователя, чтобы статус был привязан к нему
        form.instance.user = self.request.user
        return super().form_valid(form)




class TypeListView(ListView):
    model = Type
    template_name = 'cash/type_list.html'  # Шаблон для отображения списка типов
    context_object_name = 'types'

    def get_queryset(self):
        # Фильтруем типы, чтобы возвращать только те, которые принадлежат текущему пользователю
        return Type.objects.filter(user=self.request.user)

class TypeCreateView(CreateView):
    model = Type
    fields = ['name', ]  # Укажите поля, которые будут в форме
    template_name = 'cash/type_add.html'
    success_url = reverse_lazy('type_list')

    def form_valid(self, form):
        # Присваиваем текущего пользователя, чтобы тип был привязан к нему
        form.instance.user = self.request.user
        return super().form_valid(form)



class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm  # Используем форму для редактирования статуса
    template_name = 'cash/status_edit.html'
    context_object_name = 'status'

    def get_object(self):
        """Получаем статус по ID и проверяем, что он принадлежит текущему пользователю."""
        obj = get_object_or_404(Status, id=self.kwargs['pk'], user=self.request.user)
        return obj

    def get_success_url(self):
        """Перенаправляем на страницу со списком статусов после успешного редактирования."""
        return reverse_lazy('status_list')


def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)

    # Проверяем, что текущий пользователь является владельцем статуса
    if status.user == request.user:
        status.delete()
        messages.success(request, "Статус успешно удален.")
    else:
        messages.error(request, "У вас нет прав для удаления этого статуса.")

    return redirect('status_list')


class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypesForm  # Используем форму для редактирования типа
    template_name = 'cash/type_edit.html'
    context_object_name = 'type'

    def get_object(self):
        """Получаем тип по ID и проверяем, что он принадлежит текущему пользователю."""
        obj = get_object_or_404(Type, id=self.kwargs['pk'], user=self.request.user)
        return obj

    def get_success_url(self):
        """Перенаправляем на страницу со списком типов после успешного редактирования."""
        return reverse_lazy('type_list')


def type_delete(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)

    # Проверяем, что текущий пользователь является владельцем типа
    if type_obj.user == request.user:
        type_obj.delete()
        messages.success(request, "Тип успешно удален.")
    else:
        messages.error(request, "У вас нет прав для удаления этого типа.")

    return redirect('type_list')


class RecordListView(ListView):
    model = Record
    template_name = 'cash/record_list.html'  # Путь к шаблону
    context_object_name = 'records'  # Контекст, который будет доступен в шаблоне

    def get_queryset(self):
        """Показываем только записи текущего пользователя."""
        return Record.objects.filter(user=self.request.user).order_by('-created_at')

class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'cash/record_edit.html'
    context_object_name = 'record'

    def get_object(self):
        obj = get_object_or_404(Record, id=self.kwargs['pk'], user=self.request.user)
        return obj

    def get_success_url(self):
        return reverse_lazy('record_list')

def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)

    # Проверяем, что текущий пользователь является владельцем записи
    if record.user == request.user:
        record.delete()
        messages.success(request, "Запись успешно удалена.")
    else:
        messages.error(request, "У вас нет прав для удаления этой записи.")

    return redirect('record_list')




class SubcategoryListView(ListView):
    model = Category
    template_name = 'cash/subcategory_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        categories = Category.objects.filter(user=self.request.user).prefetch_related('subcategories')
        return categories

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'cash/subcategory_edit.html'
    context_object_name = 'subcategory'

    def get_object(self):
        """Получаем подкатегорию по ID и проверяем, что она принадлежит текущему пользователю."""
        obj = get_object_or_404(Subcategory, id=self.kwargs['pk'], user=self.request.user)
        return obj

    def get_success_url(self):
        """Перенаправляем на страницу со списком подкатегорий после успешного редактирования."""
        return reverse_lazy('subcategory_list')


def subcategory_delete(request, pk):
    record = get_object_or_404(Subcategory, pk=pk)

    # Проверяем, что текущий пользователь является владельцем записи
    if record.user == request.user:
        record.delete()
        messages.success(request, "Подкатегория успешно удалена.")
    else:
        messages.error(request, "У вас нет прав для удаления этой записи.")

    return redirect('subcategory_list')


class CategoryListView(ListView):
    model = Type
    template_name = 'cash/category_list.html'
    context_object_name = 'types'

    def get_queryset(self):
        types = Type.objects.filter(user=self.request.user).prefetch_related('categories')
        return types


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cash/category_edit.html'
    context_object_name = 'category'

    def get_object(self):
        """Получаем категорию по ID и проверяем, что она принадлежит текущему пользователю."""
        obj = get_object_or_404(Category, id=self.kwargs['pk'], user=self.request.user)
        return obj

    def get_success_url(self):
        """Перенаправляем на страницу со списком категорий после успешного редактирования."""
        return reverse_lazy('category_list')



def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    # Проверяем, что текущий пользователь является владельцем записи
    if category.user == request.user:
        category.delete()
        messages.success(request, "Категория успешно удалена.")
    else:
        messages.error(request, "У вас нет прав для удаления этой категории.")

    return redirect('category_list')


