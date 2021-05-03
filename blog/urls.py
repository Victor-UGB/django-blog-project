from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, register_request, login_request, logout_request


urlpatterns = [
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("logout/", views.logout_request, name= "logout"),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('', BlogListView.as_view(), name='home'),
] 