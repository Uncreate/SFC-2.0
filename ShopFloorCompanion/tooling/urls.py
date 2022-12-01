from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tool_builder/', views.tool_builder, name='tool_builder'),
]
