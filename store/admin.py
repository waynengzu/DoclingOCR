from django.contrib import admin
from . import models

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'path', 'user')
    list_editable = ('type',)

# Register your models here.
admin.site.register(models.Document, DocumentAdmin)

admin.site.register(models.Log)

admin.site.register(models.User)