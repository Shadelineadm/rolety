from . import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.home_view, name="home"),
    path('catalog/', views.catalog_view, name="catalog"),
    path('calculator/', views.calculator_view, name="calculator"),
    path('price/<str:type>/<int:pk>/<int:fab>/', views.price_view, name="price"),
    path('workers/', views.workers_view, name="workers"),
    path('net/<int:pk>/', views.net_view, name="net"),
    path('rolet/<int:pk>/', views.rolet_view, name="rolet"),
    path('net/<int:pk>/price/', views.net_price, name="net_price"),
    path('rolet/<int:pk>/price/', views.rolet_price, name="rolet_price"),
    path('fabric/<int:pk>/', views.fabric_view, name="fabric"),
]
