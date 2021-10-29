from django.contrib import admin

from .models import Tag, Project, Feedback

# Register your models here.

admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Feedback)
