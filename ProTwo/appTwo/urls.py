from django.conf.urls import url
from appTwo import views

app_name = 'appTwo'
urlpatterns = [
    url(r'^$',views.clients,name='clients'),
    url(r'^register/$', views.book,name='book'),
    url(r'^login/$',views.user_login,name='user_login')
]
