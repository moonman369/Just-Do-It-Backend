from django.contrib import admin
from .models import User, Task

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_email', 'username']
    exclude = ('password',)  # Exclude the password field from the admin interface

admin.site.register(User, UserAdmin)
admin.site.register(Task)