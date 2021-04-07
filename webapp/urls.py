from django.urls import path
from . import views

urlpatterns=[
	path('', views.open),
	path('home/', views.land),
	path('home_chart/', views.land1),
	path('reg', views.check),
	path('log_check', views.log_check),
	path('user/', views.user),
	#path('device/', views.land1),
	#path('device_log/', views.check),
	#path('village/', views.log_check),
	#path('funding_agency/', views.log_check),
	#path('user_add/', views.land1),
	#path('device_add/', views.check),
	#path('village_add/', views.log_check),
	#path('funding_agency_add/', views.log_check),
]
