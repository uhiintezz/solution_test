from __future__ import annotations

from django.urls import path

from cash.api.v1.views import (
    home,
    create_subcategory,
    create_category,
    create_type
)



urlpatterns = [
    path('home/', home, name='home'),
    path('create_subcategory/', create_subcategory, name='create_subcategory'),
    path('create_category/', create_category, name='create_category'),
    path('create_type/', create_type, name='create_type'),
]