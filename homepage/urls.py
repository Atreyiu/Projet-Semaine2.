from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    # Pages Index root
    path('', views.HomepageView.as_view(), name='homepage'),

    # register root
    path('register/', views.register, name='register'),
]

