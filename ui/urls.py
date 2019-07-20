from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.events, name='events'),
    path('add', views.event_add, name='event_add'),
    path('registration', views.registration, name='registration'),
    path('auth', views.auth, name='auth'),

    path('<event_id>', views.event, name='event'),
    path('<event_id>/change', views.event_change, name='event_change'),
   	path('<event_id>/history',views.event_history,name='event_history'),
] + static(settings.STATIC_URL);