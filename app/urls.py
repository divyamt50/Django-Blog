from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('signup/', SignupView.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('blogs/', BlogListView.as_view(), name = 'blog_list'),
    path('blogs/create/', BlogCreateView.as_view(), name = 'blog_create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name = 'blog_detail'),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('blogs/<int:pk>/update/', BlogUpdateView.as_view(), name = 'blog_update'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name = "blog_delete"),
    path('blog/<int:pk>/comment/', CommentCreateView.as_view(), name = "add_comment"),
    path('comments/<int:pk>/edit/', CommentEditView.as_view(), name = "edit_comment"),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name = "delete_comment"),
]
