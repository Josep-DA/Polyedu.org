from django.contrib import admin
from .models import NewsCategory, News, Comment

# Register your models here.
admin.site.register(NewsCategory)

class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time')

admin.site.register(News,AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display=('news','profile','comment','status')
admin.site.register(Comment,AdminComment)