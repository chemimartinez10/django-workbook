from django.urls import path

from modules.main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lists", views.lists, name="lists"),
    path("shared", views.shared, name="shared"),
    path("lists/delete/<int:id>", views.lists_delete, name="lists_delete"),
    path("tasks/<int:id>", views.tasks, name="tasks"),
    path("task_update/<int:id>/<str:done>", views.task_update, name="task_update"),
]
