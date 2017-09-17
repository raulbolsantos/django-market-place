from django.contrib import admin
from portal.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}


admin.site.register(Category, CategoryAdmin)
