from django.contrib import admin

from .models import Department, Employee, EmployeeEducation, EmployeeWorkExperience


class DepartmentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('department_id', 'name')
    search_fields = ('department_id', 'name')


class EmployeeEducationInline(admin.TabularInline):
    model = EmployeeEducation
    can_delete = True
    extra = 1
    verbose_name_plural = 'Employee Education'


class EmployeeWorkExperience(admin.TabularInline):
    model = EmployeeWorkExperience
    can_delete = True
    extra = 1


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EmployeeEducationInline, EmployeeWorkExperience]
    fields = ('employee_id', ('first_name', 'last_name'), ('email', 'phone'), ('d_o_b', 'nationality'),
              'status', ('employment', 'emp_status'))
    list_display = ('employee_id', 'first_name', 'last_name', 'email', 'phone', 'd_o_b',
                    'nationality', 'status', 'employment', 'emp_status')
    search_fields = ('employee_id', 'email', 'first_name', 'last_name', 'phone', 'nationality')
    list_filter = ('status', 'emp_status')


# Register your models here.
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)

admin.site.site_title = 'Automatic Payroll System'
admin.site.site_header = 'Automatic Payroll System'
admin.site.index_title = 'Admin Interface'
