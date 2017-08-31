from django.conf.urls import url
from grabber import views
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^$', views.grabber, name='grabber'),
    url(r'^favicon\.ico$', favicon_view),
]