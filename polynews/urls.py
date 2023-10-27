from django.urls import path
from . import views

urlpatterns = [
    # No category
    path('', views.polynews, name="polynews"),
    path('article/<int:pk>', views.newsarticle, name="newsarticle"),
    path('categories/<str:pk>', views.categories, name="categories"),

]
