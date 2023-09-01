from django.contrib import admin
from .models import models
# Register your models here.
from .models import Task

admin.site.register(Task)
