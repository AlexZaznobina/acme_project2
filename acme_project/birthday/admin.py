from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Birthday, Tag

admin.site.register(Birthday)
admin.site.unregister(Group)
admin.site.register(Tag)