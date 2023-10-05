from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.ContactCreateView.as_view(), name="contact-create"),
]
