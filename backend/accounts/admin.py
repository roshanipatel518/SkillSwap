from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'role', 'is_blocked', 'date_joined')
    list_filter = ('role', 'is_blocked', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'bio', 'location', 'profile_image')}),
        ('Skills', {'fields': ('skills_offered', 'skills_wanted', 'availability')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'is_blocked', 'is_public', 'groups', 'user_permissions')}),
        ('Rating', {'fields': ('rating', 'rating_count')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'role'),
        }),
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'reviewee', 'rating', 'text_preview', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('reviewer__email', 'reviewee__email', 'text')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Review Text'
