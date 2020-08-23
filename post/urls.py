from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('<slug>/', views.post_detail, name="post_detail"),
]
