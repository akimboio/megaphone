from django.conf.urls import url, patterns
from megaphone.tts import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'(?i)^tts/(?P<format>(aaif|wave|mp4f))$', views.tts)
)
