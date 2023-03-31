from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title","description","priority","enability","date_debut","date_expiration","to_prolong")

admin.site.register(Todo,TodoAdmin)