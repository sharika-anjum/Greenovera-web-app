from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(user)
admin.site.register(funding_agency)
admin.site.register(country)
admin.site.register(states)
admin.site.register(districts)
admin.site.register(block)
admin.site.register(village)

