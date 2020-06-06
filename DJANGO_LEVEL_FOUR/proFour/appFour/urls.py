from django.conf.urls import url
from appFour import views

#the RELATIVE can only be specified after passing in the first extension(page2)
app_name = 'appFour'
urlpatterns = [
    url(r'^relative/$', views.relative_url, name='relative_url'),
    url(r'^$', views.page2, name='page2'),
    url(r'^base/$', views.base, name='base')
]
