from django.urls import path, include

from petstagram.common import views

urlpatterns = [
    path('', views.common, name='common')
]