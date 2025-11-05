# Triple E - Educational Empowerment Platform

A comprehensive Django-based educational platform designed to empower War on Drugs impacted communities through federal contracting and cannabis compliance training programs.

## Project Overview

**Project Name:** Triple E
**Purpose:** High-converting website for economically distressed communities, with a focus on federal contracting (8(a) certification) and cannabis compliance.

**Target Users:**
- Rural Communities in economically distressed areas
- Community-Based Organizations serving formerly incarcerated populations
- Entrepreneurs pursuing 8(a) certification
- Cannabis Industry Workers transitioning to federal contracting

**Geographic Focus:** California-Oregon-Washington corridor

## Features

### Core Functionality
- ✅ User authentication and authorization (register, login, logout)
- ✅ User profile management with profile pictures
- ✅ Course catalog with search and pagination
- ✅ Course enrollment system
- ✅ User dashboard showing enrolled courses
- ✅ Testimonials with rating system (video, text, audio)
- ✅ FAQ section with expandable/collapsible answers
- ✅ Contact form with email notifications
- ✅ Comprehensive admin interface
- ✅ Responsive design with Tailwind CSS

### Data Models
- **User Profile:** Extended Django user with bio and profile picture
- **Course:** Title, description, price, duration, enrolled users
- **Testimonial:** User reviews with ratings, source types, featured flag
- **FAQ:** Questions and answers with ordering
- **Contact Message:** Form submissions tracking

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Quick Start

1. **Navigate to project directory:**
   ```bash
   cd /Users/r.kevinbloomquist/Sites/triple_e
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

4. **Access the application:**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

### Admin Access

**Username:** admin
**Password:** admin123

## Project Structure

```
triple_e/
├── accounts/           # User authentication and profiles
├── courses/            # Course management
├── testimonials/       # User testimonials
├── pages/             # Static pages (home, about, FAQ, contact)
├── triple_e_project/  # Main project settings
├── templates/         # HTML templates
├── static/           # CSS, JS, images
├── media/            # User uploads
└── manage.py         # Django management script
```

## Usage Guide

### For Administrators

1. **Log in to admin panel** at `/admin/`
2. **Add Courses:**
   - Navigate to Courses → Add Course
   - Fill in title, description, price, duration
   - Save to make available to users

3. **Manage Testimonials:**
   - Navigate to Testimonials
   - Review and approve submitted testimonials
   - Mark testimonials as "featured" to show on homepage

4. **Create FAQs:**
   - Navigate to FAQs → Add FAQ
   - Set question, answer, and order
   - Mark as active to display

5. **View Contact Messages:**
   - Navigate to Contact Messages
   - Review submissions and mark as read

### For Users

1. **Register:** Create an account at `/accounts/register/`
2. **Browse Courses:** View available courses at `/courses/`
3. **Enroll:** Click "Enroll Now" on any course detail page
4. **Dashboard:** Access your enrolled courses at `/accounts/dashboard/`
5. **Profile:** Update your profile at `/accounts/profile/`

## Key URLs

- Homepage: `/`
- About: `/about/`
- Courses: `/courses/`
- FAQ: `/faq/`
- Contact: `/contact/`
- Login: `/accounts/login/`
- Register: `/accounts/register/`
- Dashboard: `/accounts/dashboard/`
- Admin: `/admin/`

## Design Philosophy

The website follows a conversion-driven design approach inspired by Alex Melen (SmartSites):
- Trust-heavy with proof elements (stats, testimonials)
- Clean grid layouts for easy navigation
- Strong CTAs (Call-to-Actions)
- Frictionless user experience
- Mobile-responsive design

## Technologies Used

- **Backend:** Django 4.2
- **Frontend:** Tailwind CSS (via CDN)
- **Database:** SQLite (development)
- **Forms:** Django Crispy Forms with Tailwind
- **Authentication:** Django built-in auth system

## Development Notes

### Email Configuration
Currently using console email backend for development. Emails will be printed to console.

To configure real email in production, update `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email'
EMAIL_HOST_PASSWORD = 'your-password'
```

### Media Files
Profile pictures and other uploads are stored in `/media/` directory.
In production, configure proper media file serving (e.g., S3, CloudFront).

### Static Files
For production, collect static files:
```bash
python manage.py collectstatic
```

## Future Enhancements

Potential features to add:
- Payment integration for course purchases
- Course content management (lessons, modules)
- Progress tracking for enrolled courses
- Certificates upon course completion
- Discussion forums
- Live chat support
- Email marketing integration
- Analytics dashboard
- Multi-language support

## Support

For questions or issues, please contact the development team or submit a message through the contact form.

---

**Generated:** 2025
**License:** Proprietary
**Status:** Development
