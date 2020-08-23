from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'category', 'publish')
    list_editable = ('status', 'category')
    search_fields = ('body', 'title')
    list_filter = ('created', 'status', 'author', 'category')
    ordering = ('author', )
    filter_horizontal = ()
    prepopulated_fields = {"slug": ("title",)}
