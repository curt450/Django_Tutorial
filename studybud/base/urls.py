from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login")
    path('', views.home, name="home"), 
    path('room/<str:pk>/', views.room, name="room"),

    path('create-room/', veiws.createRoom, name="create-room"),
    path('update-room/<str:pk>/', veiws.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', veiws.deleteRoom, name="delete-room"),
]
