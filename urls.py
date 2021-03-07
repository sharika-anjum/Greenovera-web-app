from django.urls import path
from . import views

urlpatterns =[
    path('base',views.base_view),
    path('register1', views.register_1),
    path('register_2',views.register_2),
    path('login',views.login_1),
    path('log_ch1',views.log_ch1),
    path('index', views.index_view),
]
