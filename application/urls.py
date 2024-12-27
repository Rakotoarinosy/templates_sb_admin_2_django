from django.urls import path
from application import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('not-found/', views.not_found, name='not_found'),
    path('blank/', views.blank, name='blank'),
    path('utilities_color/', views.utilities_color, name='utilities_color'),
    path('utilities_border/', views.utilities_border, name='utilities_border'),
    path('utilities_animation/', views.utilities_animation, name='utilities_animation'),
    path('utilities_other/', views.utilities_other, name='utilities_other'),
    path('cards/', views.cards, name='cards'),
    path('buttons/', views.buttons, name='buttons'),
]
