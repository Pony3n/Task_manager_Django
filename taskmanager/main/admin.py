from django.contrib import admin
from main.models import *


class AdminTask(admin.ModelAdmin):
    list_display = ['id', 'description', 'until']

class AdminUser(admin.ModelAdmin):
    list_display = ['nick', 'email', 'password']

admin.site.register(Task, AdminTask)
admin.site.register(User, AdminUser)

