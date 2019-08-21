from . import views
from django.urls import path 

urlpatterns = [
    path('get_all_user/',views.get_all_user.as_view()),
]
