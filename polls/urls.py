from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # Pages Index root
    path('', views.IndexView.as_view(), name='index'),
    # Pages Detail root
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # Pages Results root
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # Vote root
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

