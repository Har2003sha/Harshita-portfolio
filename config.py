# Configuration File for Portfolio App
# अपनी जानकारी यहाँ update करो

# ===========================================
# PERSONAL INFORMATION
# ===========================================

PORTFOLIO_OWNER = "Harshita S"
PORTFOLIO_TITLE = "Data Science Consultant"
PORTFOLIO_EMAIL = "harshita@example.com"
PORTFOLIO_PHONE = "+91 98765 43210"
PORTFOLIO_LOCATION = "India"

# ===========================================
# SOCIAL MEDIA LINKS
# ===========================================

SOCIAL_LINKS = {
    'linkedin': 'https://linkedin.com/in/yourprofile',
    'github': 'https://github.com/yourprofile',
    'twitter': 'https://twitter.com/yourprofile',
    'instagram': 'https://instagram.com/yourprofile'
}

# ===========================================
# SITE SETTINGS
# ===========================================

DEBUG = True
PORT = 5000
TEMPLATE_FOLDER = 'templates'
STATIC_FOLDER = 'static'

# ===========================================
# PROJECT IMAGES PATH
# ===========================================

IMAGES_PATH = 'static/images/'
PROJECT_IMAGE_HEIGHT = '250px'

# ===========================================
# CONTACT SETTINGS
# ===========================================

# Email setup के लिए (optional)
EMAIL_SENDER = 'noreply@portfolio.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
ADMIN_EMAIL = 'admin@portfolio.com'

# ===========================================
# SKILLS PROFICIENCY LEVELS
# ===========================================

SKILLS = {
    'Data Analysis & Visualization': 95,
    'Machine Learning & AI': 88,
    'Python & Statistical Analysis': 92,
    'SQL & Database Design': 90,
    'Business Intelligence Tools': 85
}

# ===========================================
# EXPERIENCE SUMMARY
# ===========================================

EXPERIENCE = {
    'total_years': 5,
    'projects_completed': 20,
    'happy_clients': 50
}

# ===========================================
# SITE METADATA
# ===========================================

SITE_TITLE = "Harshita S - Data Science Consultant Portfolio"
SITE_DESCRIPTION = "Professional portfolio showcasing data science projects, skills, and expertise"
SITE_KEYWORDS = "data science, machine learning, analytics, portfolio"
AUTHOR = "Harshita S"

# ===========================================
# COLOR SCHEME (CSS में भी change करना)
# ===========================================

COLOR_PRIMARY = "#667eea"
COLOR_SECONDARY = "#764ba2"
COLOR_ACCENT = "#ffc107"
COLOR_DARK = "#2d3436"
COLOR_LIGHT = "#f8f9fa"

# ===========================================
# FEATURES TOGGLE
# ===========================================

FEATURES = {
    'enable_projects': True,
    'enable_blog': False,
    'enable_portfolio_api': True,
    'enable_analytics': False,
    'enable_comments': False,
}

# ===========================================
# PAGINATION SETTINGS
# ===========================================

ITEMS_PER_PAGE = 9
MAX_PROJECTS_ON_HOME = 3

# ===========================================
# SEO SETTINGS
# ===========================================

GOOGLE_ANALYTICS_ID = 'UA-XXXXXXXXX-X'
ROBOTS_TXT = 'User-agent: *\nDisallow: /admin'

# ===========================================
# SECURITY SETTINGS
# ===========================================

SECRET_KEY = 'your-secret-key-here-change-in-production'
ALLOWED_HOSTS = ['localhost', 'your-domain.com']
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file upload
