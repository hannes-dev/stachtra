from django.urls import path    

from . import views

app_name = 'sta'
urlpatterns = [
    path('', views.index, name='index'),
    path('import/user/<str:userid>', views.import_user, name='import_user'),
    path('import/apps/<str:userid>', views.import_apps, name='import_apps'),
    path('import/achievements/<str:userid>/<str:appid>', views.import_achievements, name='import_achievements'),
    path('user/<str:userid>', views.user, name='user'),
    path('user/<str:userid>/apps', views.apps, name='apps'),
    path('user/<str:userid>/<str:appid>', views.achievements, name='achievements'),
]