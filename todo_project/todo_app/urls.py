from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path("about/",views.about,name="about"),
    path("create/",views.create,name="create"),
    path("toggle_finished/<todo_id>",views.toggle_finished,name="toggle_finished"),
    path("delete/<Todos_id>",views.delete,name="delete"),
    path("update/<Todos_id>",views.update,name="update"),
]
