from django.conf.urls import include, url
from simplemooc.accounts.views import *
from django.contrib.auth.views import logout, login

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^nova-senha/$', password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm, name='password_reset_confirm'),
	url(r'^cadastre-se/$', register, name='register'),
    url(r'^editar/$', edit, name='edit'),
    url(r'^editar-senha/$', edit_password, name='edit_password'),
]