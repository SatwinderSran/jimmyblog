from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('<id>/post_edit/', views.post_edit, name="post_edit"),
    path('<id>/post_delete/', views.post_delete, name="post_delete"),
    path('<id>/favorite_post/', views.favorite_post, name="favorite_post"),
    path('<id>/<slug>/', views.post_detail, name="post_detail"),
    path('post_create/', views.post_create, name="post_create"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('favorites/', views.post_favorite_list, name="post_favorite_list"),
    path('about/', views.about, name="about"),
    path('contact/', views.Contact, name='contact'),    
]
