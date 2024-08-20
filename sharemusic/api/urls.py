from django.urls import path
from .views import main,home
from .views import RoomSerializerView

urlpatterns = [
  path('',RoomSerializerView.as_view())
]
