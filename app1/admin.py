from django.contrib import admin

from app1 import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
