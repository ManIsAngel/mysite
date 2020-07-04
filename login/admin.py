from django.contrib import admin
from . import models

# Register your models here.


# 注册User到Admin后台
admin.site.register(models.User)
admin.site.register(models.ConfirmString)
