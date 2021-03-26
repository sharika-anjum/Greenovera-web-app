from django.urls import path
from . import views

urlpatterns=[
	path('', views.open),
	path('home/', views.land),
	path('home_chart/', views.land1),
	path('check', views.check),
	path('log_check', views.log_check),

]
