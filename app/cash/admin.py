from django.contrib import admin
from .models import Type, Category, Subcategory, Status, Record

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Колонки для отображения в списке
    search_fields = ('name',)  #

@admin.register(Record)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'type', 'category', 'subcategory', 'created_at')  # Колонки для отображения в списке
    search_fields = ('name',)  # Поля для поиска
    list_filter = ('status', 'type', 'category', 'subcategory')