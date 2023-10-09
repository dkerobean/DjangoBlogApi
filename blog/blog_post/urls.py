from django.urls import path
from . import views


urlpatterns = [
    path('tag/create/', views.TagDetailView.as_view(), name="tag-create"),
    path('tag/list/', views.TagCreateView.as_view(), name="tag-list"),
    path('tag/delete/<int:pk>/', views.TagDetailView.as_view(), name="tag-delete"), # noqa

    path('category/list/', views.CategoryListView.as_view(), name="category-list"), # noqa
    path('category/create/', views.CategoryDetailView.as_view(), name="category-create"), # noqa
    path('category/delete/<int:pk>/', views.CategoryDetailView.as_view(), name="category-delete"), # noqa
]
