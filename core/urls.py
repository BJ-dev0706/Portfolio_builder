from django.urls import path
from . import views

urlpatterns = [
    # Home and authentication
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    
    # Skills management
    path('skills/', views.skills_manage, name='skills_manage'),
    path('skills/delete/<int:skill_id>/', views.skill_delete, name='skill_delete'),
    
    # Projects management
    path('projects/', views.projects_manage, name='projects_manage'),
    path('projects/edit/<int:project_id>/', views.project_edit, name='project_edit'),
    path('projects/delete/<int:project_id>/', views.project_delete, name='project_delete'),
    
    # Services management
    path('services/', views.services_manage, name='services_manage'),
    path('services/delete/<int:service_id>/', views.service_delete, name='service_delete'),
    
    # Experience management
    path('experiences/', views.experiences_manage, name='experiences_manage'),
    path('experiences/delete/<int:experience_id>/', views.experience_delete, name='experience_delete'),
    
    # Education management
    path('education/', views.education_manage, name='education_manage'),
    path('education/delete/<int:education_id>/', views.education_delete, name='education_delete'),
    
    # Testimonials management
    path('testimonials/', views.testimonials_manage, name='testimonials_manage'),
    path('testimonials/delete/<int:testimonial_id>/', views.testimonial_delete, name='testimonial_delete'),
    
    # Social links management
    path('social-links/', views.social_links_manage, name='social_links_manage'),
    path('social-links/delete/<int:link_id>/', views.social_link_delete, name='social_link_delete'),
    
    # Portfolio views
    path('preview/', views.portfolio_preview, name='portfolio_preview'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('export/', views.export_portfolio, name='export_portfolio'),
    
    # Public portfolio
    path('portfolio/<str:username>/', views.portfolio_detail, name='portfolio_detail'),
] 