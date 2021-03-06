from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Case, BooleanField, Value, When
from django.urls import reverse
from sta.models import App, User, Achievement
from sta.stapi import load_player, load_player_apps, load_achievements, load_player_achievements
from sta.utils import determine_user

def index(request):
    return HttpResponse("yes")

def user(request, userid):
    user = determine_user(userid)
    return render(request, "sta/user.html", {"user": user})

def apps(request, userid):
    user = determine_user(userid)
    app_list = App.objects.filter(users=user)
    return render(request, "sta/apps.html", {"app_list": app_list, "userid": user.steamid})

def achievements(request, userid, appid):
    user = determine_user(userid)
    achievements = Achievement.objects.filter(app=App.objects.get(pk=appid)).annotate(achieved=Case(When(users=user, then=Value(True)), default=Value(False), output_field=BooleanField())).order_by('-percentage')
    
    achieved = 0
    unachieved = 0
    
    for ach in achievements:
        if ach.achieved:
            achieved += 1
        else:
            unachieved += 1
            
    return render(request, "sta/achievements.html", {"ach_list": achievements, "achieved": achieved, "unachieved": unachieved, "userid": userid, "appid": appid})

def import_achievement_progress(request, userid, appid):
    load_player_achievements(userid, appid)
    return HttpResponseRedirect(reverse('sta:achievements', args=[userid, appid]))
     
def import_user(request, userid):
    load_player(userid)
    return render(request, "sta/success.html", {"item": "user"})

def import_apps(request, userid):
    load_player_apps(userid)
    return render(request, "sta/success.html", {"item": "apps"})

def import_achievements(request, userid, appid):
    load_achievements(appid)
    load_player_achievements(userid, appid)
    return HttpResponseRedirect(reverse('sta:achievements', args=[userid, appid]))
