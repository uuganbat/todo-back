from django.urls import path
from src.api import views as v


app_name = "api"
urlpatterns = [
    path("login/", v.LoginAPI.as_view(), name="login"),
    path("task-list/", v.TaskListAPI.as_view(), name="task-list"),
    path("task-create/", v.TaskCreateAPI.as_view(), name="task-create"),
    path("task-delete/", v.TaskDeleteAPI.as_view(), name="task-delete"),
]
