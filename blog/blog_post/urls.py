from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.TagDetailView.as_view(), name="tag-create"),
    path('list/', views.TagCreateView.as_view(), name="tag-list"),
    path('delete/<int:pk>/', views.TagDetailView.as_view(), name="tag-delete"), # noqa
]
