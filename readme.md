# Portfolio Builder

A comprehensive Django web application that allows users to create, customize, and manage their professional portfolios with ease. Build stunning portfolio websites with multiple themes, analytics tracking, and export capabilities.

## 🚀 Features

### Core Functionality
- **User Authentication**: Secure registration and login system
- **Profile Management**: Complete user profile with bio, contact information, and profile pictures
- **Portfolio Dashboard**: Intuitive dashboard with completion tracking and analytics overview

### Portfolio Components
- **Skills Management**: Add and organize technical skills with proficiency levels
- **Project Showcase**: Display projects with images, descriptions, GitHub links, and live demos
- **Professional Experience**: Track work history with detailed job descriptions
- **Education History**: Manage educational background and achievements
- **Services Offered**: Highlight professional services with custom icons
- **Client Testimonials**: Showcase client feedback with ratings and photos
- **Social Media Integration**: Connect all social media profiles

### Advanced Features
- **Multiple Themes**: Choose from various portfolio themes and layouts
- **Public/Private Portfolios**: Control portfolio visibility
- **Analytics Tracking**: Monitor portfolio views, clicks, and visitor engagement
- **Portfolio Export**: Export portfolio data for backup or migration
- **Responsive Design**: Mobile-friendly and modern UI using Bootstrap 5
- **Image Optimization**: Automatic image resizing and optimization

## 🛠️ Technology Stack

- **Backend**: Django 4.2.21
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Image Processing**: Pillow
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Authentication**: Django's built-in authentication system

## 📋 Requirements

- Python 3.8+
- Django 4.2.21
- Pillow 11.2.1
- django-crispy-forms 2.4
- crispy-bootstrap5 2025.4

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/BJ-dev0706/Portfolio_builder
cd Portfolio_builder
```

### 2. Create Virtual Environment
```bash
python -m venv portfolio_env
source portfolio_env/bin/activate  # On Windows: portfolio_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📖 Usage Guide

### Getting Started
1. **Register**: Create a new account or login with existing credentials
2. **Complete Profile**: Fill in your basic information, bio, and upload a profile picture
3. **Add Content**: Start adding your skills, projects, experience, and education
4. **Customize**: Choose a theme and organize your content
5. **Publish**: Make your portfolio public and share your unique URL

### Dashboard Features
- **Completion Tracker**: Monitor your portfolio completion percentage
- **Quick Stats**: View counts of skills, projects, experiences, and testimonials
- **Analytics Overview**: Track portfolio performance and visitor engagement

### Portfolio Management
- **Skills**: Add technical skills with proficiency levels (Beginner to Expert)
- **Projects**: Showcase your work with images, descriptions, and links
- **Experience**: Document your professional journey
- **Education**: Add your academic background
- **Services**: Highlight what services you offer
- **Testimonials**: Display client feedback and ratings
- **Social Links**: Connect your social media profiles

### Analytics & Export
- **View Analytics**: Track page views, unique visitors, and engagement metrics
- **Export Portfolio**: Download your portfolio data for backup or migration

## 🎨 Themes

The application supports multiple portfolio themes:
- Modern theme (default)
- Additional themes can be added through the admin interface

## 📁 Project Structure

```
portfolio_builder/
├── core/                   # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Django forms
│   ├── urls.py            # URL patterns
│   └── admin.py           # Admin configuration
├── portfolio_builder/     # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## 🔧 Configuration

### Environment Variables
For production deployment, consider setting these environment variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection string

### Media Files
User-uploaded files are stored in the `media/` directory:
- Profile pictures: `media/profile_pics/`
- Project images: `media/project_images/`
- Testimonial images: `media/testimonial_images/`
- Theme previews: `media/theme_previews/`

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving
5. Set up media file handling
6. Configure email backend for notifications
7. Set up SSL/HTTPS
8. Configure backup strategy

### Recommended Hosting
- **Heroku**: Easy deployment with PostgreSQL addon
- **DigitalOcean**: App Platform or Droplets
- **AWS**: Elastic Beanstalk or EC2
- **PythonAnywhere**: Simple Django hosting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports & Feature Requests

Please use the GitHub Issues tab to report bugs or request new features.

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review existing issues for solutions

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive UI components
- Contributors and testers who helped improve this project

---

**Happy Portfolio Building!** 🎉
