from django.urls import path
from AppMaster import views

urlpatterns = [
		path('', views.index),
]
