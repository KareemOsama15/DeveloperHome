from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('articles/', views.display_articles, name='articles'),
    path('resources/', views.display_resources, name='resources'),
    path('questions/', views.display_questions, name='questions'),

    path('create-article/', views.create_article, name='create-article'),
    path('create-resource/', views.create_resource, name='create-resource'),
    path('create-question/', views.create_question, name='create-question'),

    path('article/<int:article_id>/', views.view_article, name='view-article'),
    path('resource/<int:resource_id>/', views.view_resource, name='view-resource'),
    path('question/<int:question_id>/', views.view_question, name='view-question'),
]
