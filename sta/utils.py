from sta.models import User
from django.shortcuts import get_object_or_404

def determine_user(userid):
    if userid.isdigit() and len(userid) == 17:
        user = get_object_or_404(User, steamid=userid)
    else:
        user = get_object_or_404(User, vanity_url=userid)
        
    return user

def get_last_url_part(url):
    url = url.split("/")
    if url[-1]:
        return url[-1]
    else:
        return url[-2]