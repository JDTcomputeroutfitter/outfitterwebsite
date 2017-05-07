from django.conf.urls import include, url
from django.contrib import admin

import about.views


urlpatterns = [
    url(r'^$', about.views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about.urls')),
    url(r'^employee/', include('employee.urls')),
    url(r'^manager/', include('manager.urls')),

]
