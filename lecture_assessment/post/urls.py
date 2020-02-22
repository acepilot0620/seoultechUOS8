from django.urls import path

from . import views

urlpatterns = [
    path('', views.post, name="post"),
    path('<int:post_id>/delete', views.delete,name='delete'),
]