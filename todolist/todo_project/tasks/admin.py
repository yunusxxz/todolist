from .models import Task, Category
from django.contrib import admin


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'priority', 'status', 'due_date')
    list_filter = ('status', 'priority', 'category', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('due_date',)


# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Category)
