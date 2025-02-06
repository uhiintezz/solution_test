from __future__ import annotations

from django.urls import include, path

urlpatterns = [
    path('v1/cash/', include('cash.api.v1.urls')),
]
