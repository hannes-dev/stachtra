from django.db import models

class User(models.Model):
    steamid = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=50)
    vanity_url = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def get_avatar_url(self):
        url = self.avatar
        return f"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/{url[0:2]}/{url}"

class App(models.Model):
    appid = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=40)
    logo = models.CharField(max_length=40)
    users = models.ManyToManyField(User)

    def get_icon_url(self):
        appid = self.appid
        icon = self.icon
        return f"http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{icon}.jpg"

    def get_logo_url(self):
        appid = self.appid
        logo = self.logo
        return f"http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{logo}.jpg"

class Achievement(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=30, primary_key=True)
    display_name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    hidden = models.BooleanField()
    icon = models.CharField(max_length=50)
    gray_icon = models.CharField(max_length=50)

    def get_icon_url(self):
        appid = self.app.appid
        icon = self.icon
        return f"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/{appid}/{icon}"
    
    def get_gray_icon_url(self):
        appid = self.app.appid
        icon = self.gray_icon
        return f"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/{appid}/{icon}"

    class Meta:
        unique_together = ['name', 'app']
