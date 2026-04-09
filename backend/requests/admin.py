from django.contrib import admin
from .models import SwapRequest, SwapMessage

@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'skill_offered', 'skill_requested', 'status', 'sender_completed', 'receiver_completed', 'created_at')
    list_filter = ('status', 'sender_completed', 'receiver_completed', 'created_at')
    search_fields = ('sender__email', 'receiver__email', 'skill_offered', 'skill_requested')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

@admin.register(SwapMessage)
class SwapMessageAdmin(admin.ModelAdmin):
    list_display = ('swap_request', 'sender', 'text_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('sender__email', 'text')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Message'
