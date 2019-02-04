from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sensor_id>/', views.detail, name='detail')
]