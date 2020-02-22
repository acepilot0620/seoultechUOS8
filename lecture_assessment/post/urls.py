from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post, name="post"),
<<<<<<< HEAD
    path('<int:post_id>/delete', views.delete,name='delete'),
=======
>>>>>>> a39c3ef64714e205898f61743f9a0f6a76440362
]