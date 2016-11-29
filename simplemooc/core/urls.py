from django.conf.urls import url
from simplemooc.core.views import *
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
]
