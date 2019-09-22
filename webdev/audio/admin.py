from django.contrib import admin

# Register your models here.
from audio.models import db_design
from audio.models import speech
from audio.models import store_syn
from audio.models import speech_to_symptoms
from audio.models import speech_symptoms

admin.site.register(db_design)
admin.site.register(speech)
admin.site.register(store_syn)
admin.site.register(speech_to_symptoms)
admin.site.register(speech_symptoms)




