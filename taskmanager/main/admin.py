from django.contrib import admin
from main.models import *


class AdminTask(admin.ModelAdmin):
    list_display = ['id', 'description', 'until']

admin.site.register(Task, AdminTask)

