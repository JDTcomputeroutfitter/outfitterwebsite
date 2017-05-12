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
    url(r'^components/$', views.category_index, name='category_index'),
    url(r'(?P<cpu_id>[0-9]+)/cpu_order/$', views.cpu_order, name='cpu_order'),
    url(r'^(?P<ram_id>[0-9]+)/ram_order/$', views.ram_order, name='ram_order'),
    url(r'^(?P<hdd_id>[0-9]+)/hdd_order/$', views.hdd_order, name='hdd_order'),
    url(r'^(?P<monitor_id>[0-9]+)/monitor_order/$', views.monitor_order, name='monitor_order'),
    url(r'^(?P<videocard_id>[0-9]+)/videocard_order/$', views.videocard_order, name='videocard_order'),
    url(r'^(?P<powersupply_id>[0-9]+)/powersupply_order/$', views.powersupply_order, name='powersupply_order'),

]