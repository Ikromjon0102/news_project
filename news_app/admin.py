from django.contrib import admin
from .models import Category, News, Contact


# Register your models here.
# admin.site.register(News)
# admin.site.register(Category)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category','publish_time', 'status']
    list_filter = ['status','category', 'created_time','publish_time' ]
    prepopulated_fields = {"slug" : ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

@admin.register(Contact)
class Category(admin.ModelAdmin):
    list_display = ['name','email','message']
    list_filter = ['name','email']

# admin.site.register(Contact)
