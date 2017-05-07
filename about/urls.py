from django.conf.urls import url
from . import views

app_name = 'about'

urlpatterns = [
    # matches /about/
    url(r'^$', views.index, name='index'),
]
