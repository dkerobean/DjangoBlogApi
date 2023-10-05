from django.urls import path
from . import views


urlpatterns = [
    path('view/', views.ContactCreateView.as_view(), name="contact-view"),
    path('create/', views.ContactCreateView.as_view(), name="contact-create"),
]
