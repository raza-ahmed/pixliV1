from django.conf.urls import url

from . import views

urlpatterns = [
    # /photos/
    url(r'^$', views.index, name='index'),

    # /photos/

    url(r'^(?P<event_id>[0-9]+)$', views.detail, name='detail'),
]
