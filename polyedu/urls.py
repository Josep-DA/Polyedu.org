from django.urls import path
from . import views, consumers
from polyedu.views import conjugation_view

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]


urlpatterns = [
    # No category
    path('', views.home, name="home"),
    path('campagne', views.campagne, name="campagne"),
    path('test-page', views.test, name="test"),

    
    # User category
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('profile/follows/<int:pk>', views.follows, name='follows'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('unfollow/<int:pk>', views.unfollow, name="unfollow"),
    path('follow/<int:pk>', views.follow, name="follow"),
    path('search_user/', views.search_user, name="search_user"),    
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    path('forum/', views.forum, name='forum'),
    path('forum/category/<str:ck>', views.forumcategory, name='forumcategory'),
    path('forum/category/<str:ck>/post/<int:pk>', views.forumpost, name='forumpost'),

    path('switch-language/', views.switch_language, name='switch_language'),

    path('chat/', views.chat_room, name='chat_room'),
    
    # Courses category
    path('courses', views.courses, name="courses"),
    path('articles/correlation-lineaire', views.correlation_lineaire, name="correlation_lineaire"),
    path('articles/geometrie-analytique', views.geometrie_analytique, name="geometrie_analytique"),
    path('articles/europe', views.europe, name="europe"),
    path('articles/classesdemots', views.classesdemots, name="classesdemots"),
    path('articles/dudh1', views.dudh1, name="dudh1"),
    path('articles/gm1', views.gm1, name="gm1"),

    
    # Articles category
    path('articles/', views.articles, name="articles"),
    path('create_article', views.article_create, name="article_create"),
    path('article_like/<int:pk>', views.article_like, name="article_like"),
    path('article_show/<int:pk>', views.article_show, name="article_show"),
    path('delete_article/<int:pk>', views.delete_article, name="delete_article"),
    path('edit_article/<int:pk>', views.edit_article, name="edit_article"),
    
    # Exercices category
    path('exercices/', views.exercices, name="exercices"),
    path('exercices/<int:pk>', views.exercice_show, name="exercice_show"),
    path('exercices/conjugation/', conjugation_view, name='conjugation'),
    
    # Ressources and Bibliography
    path('bibliography', views.bibliography, name="bibliography"),
    path('bjournal', views.bjournal, name="bjournal"),
    path('ressources_externe', views.ressources_externe, name="ressources_externe"),
    path('ressources_interne', views.ressources_interne, name="ressources_interne"),
    path('code_editor', views.code_editor, name="code_editor"),
    path('periodic_table', views.periodic_table, name="periodic_table"),
    path('word_counter', views.word_counter, name="word_counter"),
    path('code_resistor', views.code_resistor, name="code_resistor"),
    path('circuit_simulator', views.circuit_simulator, name="circuit_simulator"),
    path('career_exploration', views.career_exploration, name="career_exploration"),
    path('art_studio', views.art_studio, name="art_studio"),
    path('ondes', views.ondes, name="ondes"),
    path('ellipse_lab', views.ellipse_lab, name="ellipse_lab"),
]

