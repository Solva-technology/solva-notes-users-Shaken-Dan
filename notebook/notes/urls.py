from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/<int:note_id>/", views.note_details, name="note_details"),
    path("registration/<int:user_id>/", views.user_details, name="user_details"),
    path("all_users/", views.all_users, name="all_users"),
    path("user_all_notes/<int:user_id>", views.user_all_notes, name="user_all_notes"),
    path("add_note/", views.add_note, name="add_note"),
    path("notes/<int:note_id>/edit/", views.edit_note, name="edit_note"),
    path("notes/<int:note_id>/delete/", views.delete_note, name="delete_note")
]
