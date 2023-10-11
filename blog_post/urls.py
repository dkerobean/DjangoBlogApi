from django.urls import path
from . import views


urlpatterns = [
    path('tag/create/', views.TagDetailView.as_view(), name="tag-create"),
    path('tag/list/', views.TagCreateView.as_view(), name="tag-list"),
    path('tag/delete/<int:pk>/', views.TagDetailView.as_view(), name="tag-delete"), # noqa

    path('category/list/', views.CategoryListView.as_view(), name="category-list"), # noqa
    path('category/create/', views.CategoryDetailView.as_view(), name="category-create"), # noqa
    path('category/delete/<int:pk>/', views.CategoryDetailView.as_view(), name="category-delete"), # noqa

    path('profile/view-all/', views.UserProfileView.as_view(), name="profiles"),
    path('profile/view/<int:pk>/', views.UserProfileDetailView.as_view(), name="profile-view"),
    path('profile/delete/<int:pk>/', views.UserProfileDetailView.as_view(), name="profile-delete"),

    path('blog/view-all/', views.BlogListView.as_view(), name="blog-view-all"),
    path('blog/view/<int:pk>/', views.BlogDetailView.as_view(), name="blog-view"),
]
