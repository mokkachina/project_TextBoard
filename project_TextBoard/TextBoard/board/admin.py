from django.contrib import admin

from .models import*


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('author', 'dataCreation', 'title', 'text', 'category', 'image', 'upload')
    list_filter = ('author', 'category', 'dataCreation')


admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserResponse)
