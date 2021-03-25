from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path("results/<int:run_id>/", views.results, name="results"),
    path("list", views.list_runs, name="list_runs"),
]
