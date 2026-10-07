import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='title', lookup_expr='iexact')

    class Meta:
        model = Task
        fields = ['title', 'status', 'priority']