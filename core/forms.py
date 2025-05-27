from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, HTML
from crispy_forms.bootstrap import FormActions
from .models import (
    UserProfile, Skill, Project, Service, Experience, 
    Education, Testimonial, SocialLink
)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'username',
            'email',
            'password1',
            'password2',
            FormActions(
                Submit('submit', 'Create Account', css_class='btn btn-primary btn-lg w-100')
            )
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            # Create user profile
            UserProfile.objects.create(user=user)
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'location', 'title', 'phone', 'website', 'is_public', 'theme']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'theme': forms.Select(choices=[
                ('modern', 'Modern'),
                ('classic', 'Classic'),
                ('minimal', 'Minimal'),
                ('creative', 'Creative'),
            ])
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('location', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'bio',
            'profile_picture',
            Row(
                Column('phone', css_class='form-group col-md-6 mb-0'),
                Column('website', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('theme', css_class='form-group col-md-6 mb-0'),
                Column('is_public', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Update Profile', css_class='btn btn-primary')
            )
        )


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level', 'order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('level', css_class='form-group col-md-4 mb-0'),
                Column('order', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Save Skill', css_class='btn btn-primary')
            )
        )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'github_url', 'live_url', 'technologies', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'technologies': forms.TextInput(attrs={'placeholder': 'e.g., Python, Django, JavaScript, React'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'description',
            'image',
            'technologies',
            Row(
                Column('github_url', css_class='form-group col-md-6 mb-0'),
                Column('live_url', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'order',
            FormActions(
                Submit('submit', 'Save Project', css_class='btn btn-primary')
            )
        )


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'icon', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'icon': forms.TextInput(attrs={'placeholder': 'e.g., fas fa-code, fas fa-paint-brush'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-8 mb-0'),
                Column('order', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'description',
            'icon',
            FormActions(
                Submit('submit', 'Save Service', css_class='btn btn-primary')
            )
        )


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'role', 'start_date', 'end_date', 'description', 'location', 'is_current']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('company', css_class='form-group col-md-6 mb-0'),
                Column('role', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('start_date', css_class='form-group col-md-4 mb-0'),
                Column('end_date', css_class='form-group col-md-4 mb-0'),
                Column('is_current', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'location',
            'description',
            FormActions(
                Submit('submit', 'Save Experience', css_class='btn btn-primary')
            )
        )


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'field_of_study', 'start_year', 'end_year', 'description', 'gpa']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'start_year': forms.NumberInput(attrs={'min': 1950, 'max': 2030}),
            'end_year': forms.NumberInput(attrs={'min': 1950, 'max': 2030}),
            'gpa': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '4'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'school',
            Row(
                Column('degree', css_class='form-group col-md-8 mb-0'),
                Column('gpa', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'field_of_study',
            Row(
                Column('start_year', css_class='form-group col-md-6 mb-0'),
                Column('end_year', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'description',
            FormActions(
                Submit('submit', 'Save Education', css_class='btn btn-primary')
            )
        )


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_company', 'comment', 'rating', 'client_image']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.Select(choices=[(i, f'{i} Star{"s" if i != 1 else ""}') for i in range(1, 6)])
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('client_name', css_class='form-group col-md-6 mb-0'),
                Column('client_company', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'comment',
            Row(
                Column('rating', css_class='form-group col-md-6 mb-0'),
                Column('client_image', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Save Testimonial', css_class='btn btn-primary')
            )
        )


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform', 'url', 'order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('platform', css_class='form-group col-md-6 mb-0'),
                Column('order', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'url',
            FormActions(
                Submit('submit', 'Save Social Link', css_class='btn btn-primary')
            )
        ) 