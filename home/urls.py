from django.urls import path  # type: ignore
from home import views

urlpatterns = [
    path("", views.index, name="home")
]