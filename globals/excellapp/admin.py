from django.contrib import admin

# Register your models here.
from .models import UserProfile, client, proj_sts, client_suggestion, client_request

admin.site.register(UserProfile)
admin.site.register(client)
admin.site.register(proj_sts)
admin.site.register(client_suggestion)
admin.site.register(client_request)