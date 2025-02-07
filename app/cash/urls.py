from __future__ import annotations

from django.urls import path

from .views import (
    home,
    create_subcategory,
    create_category,
    create_type,
    create_record,
    record_delete,
    get_categories,
    get_subcategories,
    StatusListView,
    StatusCreateView,
    RecordListView,
    RecordUpdateView,
    TypeListView,
    TypeCreateView,
    SubcategoryListView,

    StatusUpdateView,
    status_delete,

    TypeUpdateView,
    type_delete,

    SubcategoryUpdateView,
    subcategory_delete,

    CategoryListView,
    CategoryUpdateView,
    category_delete,
    create_categories
)



urlpatterns = [
    path('home/', home, name='home'),
    path('create_subcategory/', create_subcategory, name='create_subcategory'),
    path('create_category/', create_category, name='create_category'),
    path('create_type/', create_type, name='create_type'),

    path('create_categories/', create_categories, name='create_categories'),

    path("create_record/", create_record, name="create_record"),
    path("ajax/get_categories/", get_categories, name="get_categories"),
    path("ajax/get_subcategories/", get_subcategories, name="get_subcategories"),


    path('status_list/', StatusListView.as_view(), name='status_list'),
    path('status_add/', StatusCreateView.as_view(), name='status_add'),
    path('status_edit/<int:pk>/', StatusUpdateView.as_view(), name='status_edit'),
    path('status_delete/<int:pk>/', status_delete, name='status_delete'),

    path('record_list/', RecordListView.as_view(), name='record_list'),  # Список записей
    path('record_edit/<int:pk>/', RecordUpdateView.as_view(), name='record_edit'),  # Редактирование записи
    path('record_delete/<int:pk>/', record_delete, name='record_delete'),

    path('type_list', TypeListView.as_view(), name='type_list'),
    path('type_add/', TypeCreateView.as_view(), name='type_add'),
    path('type_edit/<int:pk>/', TypeUpdateView.as_view(), name='type_edit'),
    path('type_delete/<int:pk>/', type_delete, name='type_delete'),

    path('subcategory_list/', SubcategoryListView.as_view(), name='subcategory_list'),
    path('subcategory_edit/<int:pk>/', SubcategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategory_delete/<int:pk>/', subcategory_delete, name='subcategory_delete'),

    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category_delete/<int:pk>/', category_delete, name='category_delete'),

]