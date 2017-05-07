from django.conf.urls import url
from . import views

app_name = 'employee'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^employee_profile/$', views.employee_profile, name='employee_profile'),
]