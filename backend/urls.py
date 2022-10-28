from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_routes),
    path('advocates/', views.all_advocates),
    path('advocates/<str:username>', views.get_advocate),
]