from django.contrib import admin
from .models import Post

# In this class inherited from ModelAdmin we can include info about how to
# display the model in the site and how to interact with it
@admin.register(Post) # decorator same as admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author') # filter option on right side
    search_fields = ('title', 'body') # search options
    prepopulated_fields = {'slug': ('title',)} # slug field now will be prepolulated from title
    raw_id_fields = ('author',) # easier search widget with ability to reference value by id
    date_hierarchy = 'publish' # date order by
    ordering = ('status', 'publish') # default ordering fields
