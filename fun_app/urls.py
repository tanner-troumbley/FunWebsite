from django.urls import path
from . import views

urlpatterns = [
    path("api", views.api_tree_view, name="api_list"),
    path("api/delete/<int:id>", views.api_delete, name="api_delete")
]