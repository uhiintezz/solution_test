from __future__ import annotations

from django_filters.rest_framework import filterset

from study.models import Lesson


class LessonsListFilterSet(filterset.FilterSet):
    class Meta:
        model = Lesson
        fields = ('product_id', )
