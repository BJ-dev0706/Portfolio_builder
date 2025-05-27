from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
import zipfile
import os
from io import BytesIO

from .models import (
    UserProfile, Skill, Project, Service, Experience, 
    Education, Testimonial, SocialLink, Theme, PortfolioAnalytics
)
from .forms import (
    CustomUserCreationForm, UserProfileForm, SkillForm, ProjectForm,
    ServiceForm, ExperienceForm, EducationForm, TestimonialForm, SocialLinkForm
)


def home(request):
    """Home page with featured portfolios"""
    featured_profiles = UserProfile.objects.filter(
        is_public=True
    ).select_related('user').order_by('-created_at')[:6]
    
    context = {
        'featured_profiles': featured_profiles,
        'total_users': User.objects.count(),
        'total_portfolios': UserProfile.objects.filter(is_public=True).count(),
    }
    return render(request, 'core/home.html', context)


def register(request):
    """User registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to Portfolio Builder.')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    """User dashboard with portfolio overview"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Calculate completion percentage
    completion_items = [
        profile.bio,
        profile.title,
        profile.location,
        request.user.skills.exists(),
        request.user.projects.exists(),
        request.user.experiences.exists(),
    ]
    completion_percentage = (sum(bool(item) for item in completion_items) / len(completion_items)) * 100
    
    # Get recent analytics
    today = timezone.now().date()
    analytics, created = PortfolioAnalytics.objects.get_or_create(
        user=request.user, 
        date=today,
        defaults={'page_views': 0, 'unique_visitors': 0}
    )
    
    context = {
        'profile': profile,
        'completion_percentage': completion_percentage,
        'skills_count': request.user.skills.count(),
        'projects_count': request.user.projects.count(),
        'experiences_count': request.user.experiences.count(),
        'testimonials_count': request.user.testimonials.count(),
        'analytics': analytics,
    }
    return render(request, 'core/dashboard.html', context)


@login_required
def profile_edit(request):
    """Edit user profile"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'core/profile_edit.html', {'form': form})


@login_required
def skills_manage(request):
    """Manage skills"""
    skills = request.user.skills.all()
    
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('skills_manage')
    else:
        form = SkillForm()
    
    return render(request, 'core/skills_manage.html', {'skills': skills, 'form': form})


@login_required
def skill_delete(request, skill_id):
    """Delete a skill"""
    skill = get_object_or_404(Skill, id=skill_id, user=request.user)
    skill.delete()
    messages.success(request, 'Skill deleted successfully!')
    return redirect('skills_manage')


@login_required
def projects_manage(request):
    """Manage projects"""
    projects = request.user.projects.all()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('projects_manage')
    else:
        form = ProjectForm()
    
    return render(request, 'core/projects_manage.html', {'projects': projects, 'form': form})


@login_required
def project_edit(request, project_id):
    """Edit a project"""
    project = get_object_or_404(Project, id=project_id, user=request.user)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('projects_manage')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'core/project_edit.html', {'form': form, 'project': project})


@login_required
def project_delete(request, project_id):
    """Delete a project"""
    project = get_object_or_404(Project, id=project_id, user=request.user)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('projects_manage')


@login_required
def services_manage(request):
    """Manage services"""
    services = request.user.services.all()
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            messages.success(request, 'Service added successfully!')
            return redirect('services_manage')
    else:
        form = ServiceForm()
    
    return render(request, 'core/services_manage.html', {'services': services, 'form': form})


@login_required
def service_delete(request, service_id):
    """Delete a service"""
    service = get_object_or_404(Service, id=service_id, user=request.user)
    service.delete()
    messages.success(request, 'Service deleted successfully!')
    return redirect('services_manage')


@login_required
def experiences_manage(request):
    """Manage experiences"""
    experiences = request.user.experiences.all()
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            messages.success(request, 'Experience added successfully!')
            return redirect('experiences_manage')
    else:
        form = ExperienceForm()
    
    return render(request, 'core/experiences_manage.html', {'experiences': experiences, 'form': form})


@login_required
def experience_delete(request, experience_id):
    """Delete an experience"""
    experience = get_object_or_404(Experience, id=experience_id, user=request.user)
    experience.delete()
    messages.success(request, 'Experience deleted successfully!')
    return redirect('experiences_manage')


@login_required
def education_manage(request):
    """Manage education"""
    education_list = request.user.education.all()
    
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            messages.success(request, 'Education added successfully!')
            return redirect('education_manage')
    else:
        form = EducationForm()
    
    return render(request, 'core/education_manage.html', {'education_list': education_list, 'form': form})


@login_required
def education_delete(request, education_id):
    """Delete an education entry"""
    education = get_object_or_404(Education, id=education_id, user=request.user)
    education.delete()
    messages.success(request, 'Education deleted successfully!')
    return redirect('education_manage')


@login_required
def testimonials_manage(request):
    """Manage testimonials"""
    testimonials = request.user.testimonials.all()
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Testimonial added successfully!')
            return redirect('testimonials_manage')
    else:
        form = TestimonialForm()
    
    return render(request, 'core/testimonials_manage.html', {'testimonials': testimonials, 'form': form})


@login_required
def testimonial_delete(request, testimonial_id):
    """Delete a testimonial"""
    testimonial = get_object_or_404(Testimonial, id=testimonial_id, user=request.user)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted successfully!')
    return redirect('testimonials_manage')


@login_required
def social_links_manage(request):
    """Manage social links"""
    social_links = request.user.social_links.all()
    
    if request.method == 'POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            social_link = form.save(commit=False)
            social_link.user = request.user
            social_link.save()
            messages.success(request, 'Social link added successfully!')
            return redirect('social_links_manage')
    else:
        form = SocialLinkForm()
    
    return render(request, 'core/social_links_manage.html', {'social_links': social_links, 'form': form})


@login_required
def social_link_delete(request, link_id):
    """Delete a social link"""
    social_link = get_object_or_404(SocialLink, id=link_id, user=request.user)
    social_link.delete()
    messages.success(request, 'Social link deleted successfully!')
    return redirect('social_links_manage')


def portfolio_detail(request, username):
    """Public portfolio view"""
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user, is_public=True)
    
    # Track analytics
    today = timezone.now().date()
    analytics, created = PortfolioAnalytics.objects.get_or_create(
        user=user,
        date=today,
        defaults={'page_views': 0, 'unique_visitors': 0}
    )
    analytics.page_views += 1
    analytics.save()
    
    context = {
        'profile': profile,
        'user': user,
        'skills': user.skills.all(),
        'projects': user.projects.all(),
        'services': user.services.all(),
        'experiences': user.experiences.all(),
        'education': user.education.all(),
        'testimonials': user.testimonials.all(),
        'social_links': user.social_links.all(),
    }
    
    # Use theme-specific template if available
    template_name = f'portfolios/{profile.theme}.html'
    try:
        return render(request, template_name, context)
    except:
        return render(request, 'portfolios/modern.html', context)


@login_required
def portfolio_preview(request):
    """Preview portfolio"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    context = {
        'profile': profile,
        'user': request.user,
        'skills': request.user.skills.all(),
        'projects': request.user.projects.all(),
        'services': request.user.services.all(),
        'experiences': request.user.experiences.all(),
        'education': request.user.education.all(),
        'testimonials': request.user.testimonials.all(),
        'social_links': request.user.social_links.all(),
        'is_preview': True,
    }
    
    template_name = f'portfolios/{profile.theme}.html'
    try:
        return render(request, template_name, context)
    except:
        return render(request, 'portfolios/modern.html', context)


@login_required
def analytics_view(request):
    """Portfolio analytics"""
    analytics = request.user.analytics.all()[:30]  # Last 30 days
    
    total_views = sum(a.page_views for a in analytics)
    total_visitors = sum(a.unique_visitors for a in analytics)
    
    context = {
        'analytics': analytics,
        'total_views': total_views,
        'total_visitors': total_visitors,
    }
    return render(request, 'core/analytics.html', context)


@login_required
def export_portfolio(request):
    """Export portfolio as static files"""
    # This is a simplified version - in production, you'd want to generate actual static files
    profile = get_object_or_404(UserProfile, user=request.user)
    
    # Create a zip file in memory
    zip_buffer = BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Add a simple HTML file
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{request.user.get_full_name() or request.user.username} - Portfolio</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <h1>{request.user.get_full_name() or request.user.username}</h1>
                <p class="lead">{profile.title}</p>
                <p>{profile.bio}</p>
                <p><strong>Location:</strong> {profile.location}</p>
                <p><strong>Email:</strong> {request.user.email}</p>
                <p><strong>Phone:</strong> {profile.phone}</p>
                <p><strong>Website:</strong> <a href="{profile.website}">{profile.website}</a></p>
            </div>
        </body>
        </html>
        """
        zip_file.writestr('index.html', html_content)
        zip_file.writestr('README.txt', 'This is your exported portfolio. Open index.html in a web browser.')
    
    zip_buffer.seek(0)
    
    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{request.user.username}_portfolio.zip"'
    
    return response
