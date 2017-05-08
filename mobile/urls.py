from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^get_interests', views.get_interests, name='get_interests'),
    url(r'^save_interests', views.save_interests, name='save_interests'),
    url(r'^add_post', views.add_post, name='add_post'),
    url(r'^get_timeline', views.get_timeline, name='get_timeline'),
]
