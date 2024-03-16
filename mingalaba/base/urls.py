from django.urls import path

from . import views

urlpatterns = [
    path('gtimg/<int:image_id>', views.load_image, name="load_image"),
]