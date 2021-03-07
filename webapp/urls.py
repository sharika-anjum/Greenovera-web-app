from django.urls import path
from . import views

urlpatterns=[
	path('', views.open),
	path('home/', views.land),

]
