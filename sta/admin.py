from django.contrib import admin
from sta.models import User, App, Achievement

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_avatar_url')

class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'appid')

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'description', 'app')

admin.site.register(User, UserAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(Achievement, AchievementAdmin)