from django.urls import path,re_path
from . import views
from django.views.generic.base import RedirectView

favicon_view=RedirectView.as_view(url="/templates",permanent=True)

urlpatterns = [
    path('',views.index,name="index"),
    re_path(r'^favicon\.ico$',favicon_view),
    path("about/",views.about,name="about"),
    path("create/",views.create,name="create"),
    path("toggle_finished/<todo_id>",views.toggle_finished,name="toggle_finished"),
    path("delete/<Todos_id>",views.delete,name="delete"),
    path("update/<Todos_id>",views.update,name="update"),
]
