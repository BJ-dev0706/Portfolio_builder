from django.contrib import admin
from .models import (
    UserProfile, Skill, Project, Service, Experience, 
    Education, Testimonial, SocialLink, Theme, PortfolioAnalytics
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'location', 'is_public', 'theme', 'created_at']
    list_filter = ['is_public', 'theme', 'created_at']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'title']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'level', 'order']
    list_filter = ['level']
    search_fields = ['name', 'user__username']
    list_editable = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'order']
    list_filter = ['created_at']
    search_fields = ['title', 'description', 'user__username']
    list_editable = ['order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'order']
    search_fields = ['name', 'description', 'user__username']
    list_editable = ['order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'user', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date']
    search_fields = ['role', 'company', 'user__username']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'user', 'start_year', 'end_year']
    list_filter = ['start_year']
    search_fields = ['degree', 'school', 'user__username']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['client_name', 'client_company', 'user__username']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'user', 'url', 'order']
    list_filter = ['platform']
    search_fields = ['user__username', 'url']
    list_editable = ['order']


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'display_name']


@admin.register(PortfolioAnalytics)
class PortfolioAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'page_views', 'unique_visitors', 'project_clicks', 'contact_clicks']
    list_filter = ['date']
    search_fields = ['user__username']
    readonly_fields = ['date']
