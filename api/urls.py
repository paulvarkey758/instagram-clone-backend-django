from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.registerView,name='register'),
    path('show/',views.showData,name='show'),
    path('login/',views.loginView,name="login"),
    path('fetch-profile/<str:tkn>/',views.fetchProfile,name="fetch-profile"),
    path('fetch-feed/',views.fetchFeed,name="fetch-feed"),
]