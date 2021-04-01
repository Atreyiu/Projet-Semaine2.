from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    # Pages Login root
    path('', views.LoginView.as_view(), name='login'),

]

