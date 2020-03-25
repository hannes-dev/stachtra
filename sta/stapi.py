import requests
import os
from sta.models import App, User, Achievement
from sta.utils import determine_user, get_last_url_part

KEY = os.getenv('STA_KEY')
ID = os.getenv('STA_STEAMID')

def user_stats_for_game(appid, key=KEY, steamid=ID):
    return requests.get(f"https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?key={key}&steamid={steamid}&appid={appid}")

def get_scema_for_game(appid, key=KEY):
    return requests.get(f"https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={key}&appid={appid}")

def get_player_achievements(appid, key=KEY, steamid=ID):
    return requests.get(f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/?key={key}&steamid={steamid}&appid={appid}")

def get_player_summary(steamid=ID, key=KEY):
    return requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={key}&steamids={steamid}")

def get_owned_games(steamid=ID, key=KEY, app_info=True):
    app_info = int(app_info)
    return requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={key}&steamid={steamid}&include_appinfo={app_info}")

### Imports ###

def load_player(steamid=ID):
    player = get_player_summary(steamid).json()['response']['players'][0]
    user = User(
        steamid=steamid,
        name=player['personaname'],
        avatar=get_last_url_part(player['avatar']),
        vanity_url=get_last_url_part(player['profileurl']),
    )
    user.save()

def load_player_apps(steamid=ID):
    apps = get_owned_games(steamid).json()['response']['games']
    for app in apps:
        app_data = App(
            appid=app['appid'],
            name=app['name'],
            icon=app['img_icon_url'],
            logo=app['img_logo_url']
        )
        app_data.save()
        app_data.users.add(User.objects.get(pk=steamid))

def load_achievements(appid):
    app = App.objects.get(appid=appid)
    achievements = get_scema_for_game(appid).json()['game']['availableGameStats']['achievements']
    for ach in achievements:
        achievement = Achievement(
            app=app,
            name=ach['name'],
            display_name=ach['displayName'],
            description=ach.get('description', ''),
            hidden=ach['hidden'] == 1,
            icon=get_last_url_part(ach['icon']),
            gray_icon=get_last_url_part(ach['icongray']),
        )
        achievement.save()

def load_player_achievements(steamid, appid):
    user = determine_user(steamid)
    achievements = get_player_achievements(appid, steamid=steamid).json()['playerstats']['achievements']
    for ach in achievements:
        if ach['achieved'] == 1:
            saved_ach = Achievement.objects.get(name=ach['apiname'])
            saved_ach.users.add(user)