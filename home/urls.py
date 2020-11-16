from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('postComments', views.postComments, name='postComments'),
    path('signup', views.signupUser, name='signupUser'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),
    path('about', views.about, name='about'),
    path('<str:slug>', views.post, name='post')
]