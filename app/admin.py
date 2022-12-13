from django.contrib import admin
from .models import Post

# Admin 
# Login: admin 
# Password: admin
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ADDING POST', {'fields': ['title']}),
        (None, {'fields': ['body']}),
        (None, {'fields': ['date']}),
    ]
    list_display = ('title', 'body', 'date')

admin.site.register(Post, PostAdmin)
