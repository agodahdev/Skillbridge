from django.contrib import admin
from .models import SkillService, BookingRequest


@admin.register(SkillService)
class SkillServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'category', 'rate_per_hour',
                    'is_approved')
    list_filter = ('is_approved', 'category',)
    search_fields = ('title', 'description', 'provider__username')
    actions = ['approve_services']

    def approve_services(self, request, queryset):
        queryset.update(is_approved=True)
    approve_services.short_description = "Approve selected services"


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'client', 'requested_date',
                    'status', 'created_at')
    list_filter = ('status', 'requested_date')
    search_fields = ('client_username', 'service__title')
