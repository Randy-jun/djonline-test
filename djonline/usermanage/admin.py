from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from usermanage.models import employee,organization
# Register your models here.

class EmployeeInline(admin.StackedInline):
    model = employee
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(UserAdmin):
    inlines = (EmployeeInline,)

admin.site.register(organization)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

