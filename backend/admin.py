from django.contrib import admin
from .models import Advocate


@admin.register(Advocate)
class AuthorAdmin(admin.ModelAdmin):
    pass
