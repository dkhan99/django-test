from django.urls import path
from django.urls.resolvers import URLPattern
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
