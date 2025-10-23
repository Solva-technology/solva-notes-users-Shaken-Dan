import os

from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, User, UserProfile
from .forms import AddNote

def home(request):
    notes = Note.objects.select_related('author', 'status').prefetch_related('categories')
    return render(request, "notes/home.html", {"notes": notes})

def note_details(request, note_id:int):
    details = get_object_or_404(
        Note.objects.select_related('author', 'status', 'author__userprofile'),
        pk=note_id)
    return render(request, "notes/note_details.html", {"details": details})

def user_details(request, user_id:int):
    details_user = get_object_or_404(User.objects, pk=user_id)

    try:
        details_userprofile = UserProfile.objects.values('bio', 'birth_date').get(user_id=user_id)
    except UserProfile.DoesNotExist:
        details_userprofile = None

    notes_list = Note.objects.filter(author_id=user_id).select_related('status')
    return render(
        request,
        "notes/user_details.html",
        {
            "details_user":details_user,
            "details_userprofile": details_userprofile,
            "notes_list": notes_list
        }
    )

def all_users(request):
    users=User.objects.all()
    return render(request, "notes/all_users.html", {"users": users})

def user_all_notes(request, user_id:int):
    user = get_object_or_404(User, id=user_id)
    notes = Note.objects.filter(author=user).order_by('-created_at')

    return render(request, "notes/user_all_notes.html", {"notes": notes})


def add_note(request):
    if request.method == 'POST':
        form = AddNote(request.POST or None)
        if form.is_valid():
            note=form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect("notes:home")
    else:
        form = AddNote()
    return render(request, "notes/add_note.html", {"form": form})

def edit_note(request, note_id:int):
    # Получает объект из бд
    note_from_db = get_object_or_404(Note, pk=note_id)

    if note_from_db.author != request.user:
        return HttpResponseForbidden("Нет прав для правки!")

    if request.method == 'POST':
        # Сохраняет измененную форму
        form = AddNote(request.POST, instance=note_from_db)
        if form.is_valid():
            form.save()
            return redirect("notes:note_details", note_id=note_id)
    else:
        # Загружает в форму заметку из бд
        form = AddNote(instance=note_from_db)

    return render(
        request,
        "notes/edit_note.html",
        {"form":form}
    )

def delete_note(request, note_id:int):

    note_to_delete = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        note_to_delete.delete()

        return redirect("notes:home")

    return render(request, "notes/delete_note.html", {"note_id":note_id})