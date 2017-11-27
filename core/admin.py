from django.contrib import admin

from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('department_id', 'name')
    search_fields = ('department_id', 'name')


# Register your models here.
admin.site.register(Department, DepartmentAdmin)
