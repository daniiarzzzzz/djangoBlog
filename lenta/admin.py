from django.contrib import admin
from django.contrib.auth.models import Group

from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.unregister(Group)
# admin.site.unregister(User)
