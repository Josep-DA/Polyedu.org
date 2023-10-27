from django.urls import path, reverse
from . import views

urlpatterns = [
    # No category
    path('', views.polyshop, name="polyshop"),
    path('catalogue/', views.catalogue, name="catalogue"),
    path('item/<int:pk>', views.item, name="item"),
    path('locations/', views.locations, name="locations"),
]
