from django.urls import path
from . import views


urlpatterns = [
    path('view/', views.ContactListView.as_view(), name="contact-view"),
    path('create/', views.ContactListView.as_view(), name="contact-create"),
    path('get/<int:pk>/', views.ContactDetailView.as_view(), name="contact-detail"), # noqa
    path('delete/<int:pk>/', views.ContactDetailView.as_view(), name="contact-delete"), # noqa
]
