# howdy/urls.py
from django.urls import path
# from django.conf.urls import path, include
from howdy import views
# from howdy.views import Home

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='home'), # Add this /about/ route
]
