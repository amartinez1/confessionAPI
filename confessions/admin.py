from django.contrib import admin

from .models import Category, Confession, User, Like


class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_date'
    fields = ['name']
    list_display = ['name', 'created_date', 'updated_date']
    list_filter = ['name', 'created_date', 'updated_date']
    search_fields = ['name']


class ConfessionAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_date'
    fields = ('title', 'content', 'score', 'category', 'user')
    list_display = ['id', 'title', 'score', 'category', 'user', 'created_date', 'updated_date']
    list_display_links = ['id', 'title', 'category', 'user']
    list_filter = ['title', 'user', 'category', 'user','created_date', 'updated_date']
    search_fields = ['id', 'title', 'category', 'user', 'created_date', 'updated_date']


class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_date'
    fields = ['device_id']
    list_display = ['device_id', 'created_date', 'updated_date']
    list_display_links = ['device_id']
    search_fields = ['device_id', 'created_date', 'updated_date']


class LikeAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_date'
    fields = ['user', 'confession']
    list_display = ('user', 'confession', 'created_date', 'updated_date')
    list_display_links = ('user', 'confession')
    search_fields = ['user', 'confession', 'created_date', 'updated_date']

admin.site.register(Confession, ConfessionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Like, LikeAdmin)
