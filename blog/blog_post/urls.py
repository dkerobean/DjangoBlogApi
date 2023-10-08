from django.urls import path
from . import views


urlpatterns = [
    path('tcreate/', views.TagDetailView.as_view(), name="tag-create"),
    path('list/', views.TagCreateView.as_view(), name="tag-list"),
    path('delete/<int:pk>/', views.TagDetailView.as_view(), name="tag-delete"), # noqa

    path('category/list/', views.CategoryListView.as_view(), name="category-list"),
    path('category/create/', views.CategoryDetailView.as_view(), name="category-create"),
    path('category/delete/<int:pk>/', views.CategoryDetailView.as_view(), name="category-delete"),
]
