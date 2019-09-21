from django.contrib import admin

# Register your models here.
from audio.models import db_design
from audio.models import speech
from audio.models import store_syn


admin.site.register(db_design)
admin.site.register(speech)
admin.site.register(store_syn)