from django.conf.urls import url
from . import views

app_name = 'manager'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user>[0-9]+)/$', views.customer_details, name='customer_details'),
    url(r'^manager_profile/$', views.manager_profile, name='manager_profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_customer/$', views.register_customer, name='register_customer'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^customer_index/$', views.customer_index, name='customer_index'),
    url(r'^register_department/$', views.register_department, name='register_department'),
]