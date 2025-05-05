from django.urls import path, re_path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    re_path(r'detail/(?P<post_slug>[-\w]+)/', views.DetailView.as_view(), name='detail'),
    path('about-us/', views.AboutUsView.as_view(), name='about'),
]