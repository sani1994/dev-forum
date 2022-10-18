from django.urls import path
from post_app.views import post_create_view


urlpatterns = [
    path('post/create', post_create_view, name='create-post'),
]