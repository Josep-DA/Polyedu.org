from django.urls import path
from . import views

urlpatterns = [
    # No category
    path('', views.polynews, name="polynews"),
    path('article/<int:pk>', views.newsarticle, name="newsarticle"),
    path('categories/<str:pk>', views.categories, name="categories"),
    path('love/', views.love_generator, name="love"),
    path('love/<str:dt>', views.love, name="love"),

]
