from django.contrib import admin
from .models import UserProfile, Note, Status, Category
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'email',
        'is_staff'
    )
    search_fields = ('name', 'email')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bio',
        'birth_date'
    )
    search_fields = ('user__username', 'bio')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'created_at'
    )
    search_fields = ('created_at', )
    filter_horizontal = ('categories', )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_final'
    )
    search_fields = ('is_final', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description'
    )
    search_fields = ('title', )