from django.urls import path
from . import views

app_name = "oneview_page"
urlpatterns = [
    path("index/", views.oneview_page, name="index"),
]
