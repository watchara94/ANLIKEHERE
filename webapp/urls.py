from . import views
from django.urls import path 

app_name = 'webapp'
urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('action/<str:id>',views.action, name='action'),
    path('registration/',views.registration, name='regis'),
    path('infor/',views.infor, name='infor'),
]
