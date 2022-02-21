from django.contrib import admin
from .models import Post

@admin.register(Post) # registers model as admin Model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # automatically sets slug name to title field value and data (if there are duplicates)
    prepopulated_fields = {'slug': ('title',)} 
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
