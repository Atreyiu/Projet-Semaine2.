from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    # Pages Login root
    path('', views.RegistrationView.as_view(), name='login'),

]

