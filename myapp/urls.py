from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('add', views.add_todo, name='add'),
    path('delete/<int:id>', views.delete_todo, name='delete'),
    path('change-status/<int:id>/<str:status>', views.change_todo, name='change-status'),
    path('logout', views.signout, name='logout'),
]