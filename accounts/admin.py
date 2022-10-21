from django.contrib import admin

# Register your models here.
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date_added')
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title',]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')
    list_filter = ("name",)
    search_fields = ['name', 'body']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
