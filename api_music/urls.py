
from django.urls import path
from .views import RoomView, Home

urlpatterns = [
    path('', Home), 
    path('api/room', RoomView.as_view())  #take this class give the view
    
]
