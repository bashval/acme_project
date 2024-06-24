from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomepageTemplateView.as_view(), name='homepage'),
]
