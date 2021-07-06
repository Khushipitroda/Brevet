from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/', views.about, name="about"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^portfolio/', views.portfolio, name="portfolio"),
    url(r'^team/', views.team, name="team"),
    path('view_product/<int:myid>/', views.view_product, name="view_product"),
    url(r'view_screen_chemicals/', views.view_screen_chemicals, name="view_screen_chemicals"),

    path('view_other_product/<int:myid>/', views.view_other_product, name="view_other_product"),
]