from django.contrib import admin
from sta.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_avatar_url')

admin.site.register(User, UserAdmin)