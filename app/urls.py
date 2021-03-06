from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.get_name, name='get_name'),
    url(r'^register/$', views.register, name='register'),
    url(r'^test/$', views.test, name='test'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
]
