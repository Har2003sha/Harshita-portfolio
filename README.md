# 🎯 Harshita S - Data Science Portfolio Application

Ek complete, interactive, aur mobile-responsive portfolio application jo Flask, HTML, CSS, JavaScript aur Bootstrap se banaya gaya hai.

## ✨ Features

### 🎨 Frontend
- **Responsive Design**: Mobile aur Desktop dono pe perfect
- **Bootstrap 5**: Latest Bootstrap framework
- **Interactive Elements**: Smooth animations aur hover effects
- **Modern UI**: Beautiful gradients aur color schemes
- **Icons**: Bootstrap Icons se professional look

### 📄 Pages/Components
1. **Home (/)** - Landing page with featured projects
2. **Info (/info)** - Professional information aur skills
3. **About Me (/aboutme)** - Personal introduction aur vision
4. **Projects (/projects)** - Sab projects ka showcase
5. **Project Detail (/project/<id>)** - Individual project details
6. **Contact (/contact)** - Contact form aur information

### 🛠️ Backend (Flask)
- RESTful API endpoints
- Dynamic content rendering
- Contact form handling
- Project data management
- JSON response support

### 📱 Mobile Features
- Mobile-first responsive design
- Touch-friendly navigation
- Optimized images
- Fast loading

## 📋 Requirements

```
Flask==2.3.3
Werkzeug==2.3.7
```

## 🚀 Installation & Setup

### Step 1: Project Structure Setup
```bash
cd d:\harshita portfolio\portfolio_app
```

### Step 2: Install Dependencies
```bash
# Windows
pip install -r requirements.txt

# ya agar virtual environment use kar rahe ho
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Add Project Images
Project images ko is path mein add karo:
```
portfolio_app/static/images/
    - project1.jfif
    - project2.jfif
    - project3.jfif
```

### Step 4: Run the Application
```bash
python app.py
```

Application shuru ho jaayega: `http://localhost:5000`

## 📁 Project Structure

```
portfolio_app/
├── app.py                    # Flask application main file
├── requirements.txt          # Python dependencies
│
├── templates/                # HTML Templates
│   ├── base.html            # Base template with navbar aur footer
│   ├── index.html           # Home page
│   ├── home.html            # Home route
│   ├── info.html            # Professional info
│   ├── aboutme.html         # About me page
│   ├── projects.html        # Projects listing
│   ├── project_detail.html  # Individual project
│   └── contact.html         # Contact page
│
├── static/                   # Static files
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   ├── js/
│   │   └── main.js          # JavaScript functionality
│   └── images/              # Project images
│       ├── project1.jfif
│       ├── project2.jfif
│       └── project3.jfif
```

## 🎯 Routes Available

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/home` | GET | Home page alternate |
| `/info` | GET | Professional info |
| `/aboutme` | GET | About me page |
| `/projects` | GET | All projects |
| `/project/<id>` | GET | Individual project |
| `/contact` | GET | Contact page |
| `/api/contact` | POST | Submit contact form |

## 🎨 Customization

### Colors Customize Karna
`static/css/style.css` mein edit karo:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --warning-color: #ffc107;
    --dark-color: #2d3436;
}
```

### Projects Data
`app.py` mein `projects` list edit karo:
```python
projects = [
    {
        'id': 1,
        'title': 'Project Name',
        'description': 'Description',
        'technologies': ['Tech1', 'Tech2'],
        'image': 'project1.jfif',
        'details': 'Full details...'
    },
    ...
]
```

### About Information
`app.py` mein `about_info` dictionary edit karo

## 💻 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Framework**: Bootstrap 5
- **Icons**: Bootstrap Icons
- **Backend**: Python Flask
- **Server**: Flask Development Server

## 📱 Responsive Breakpoints

- **Mobile**: < 576px
- **Tablet**: 576px - 992px
- **Desktop**: > 992px

## 🎬 Features in Detail

### Home Page
- Animated hero section
- Statistics display
- Featured projects preview
- Call-to-action buttons

### Projects Page
- Grid layout with cards
- Project thumbnails
- Technology badges
- Hover effects

### Project Detail Page
- Full project information
- Technologies used
- Challenges & solutions
- Results & impact
- Call to action

### Contact Page
- Contact form
- Form validation
- Contact information
- Social links
- FAQ section

## 🔧 Customization Tips

1. **Colors**: `style.css` mein CSS variables change karo
2. **Fonts**: Google Fonts integrate kar sakte ho
3. **Content**: `app.py` mein data update karo
4. **Images**: `static/images/` mein apni images add karo
5. **Animations**: `main.js` aur `style.css` mein animations customize karo

## 📊 Performance Optimization

- Minified CSS aur JavaScript
- Image optimization recommended
- Lazy loading implementation
- Smooth scrolling
- Efficient animations

## 🐛 Troubleshooting

### Images not showing
- Check `static/images/` folder path
- Image names exactly match `app.py` mein
- Image format: `.jfif`, `.jpg`, `.png`

### Port already in use
```bash
# Port change karna
app.run(debug=True, port=8000)
```

### CSS not loading
- Clear browser cache (Ctrl+F5)
- Check static file path

## 📝 Development Tips

1. **Debug Mode**: `app.run(debug=True)` - automatically reload on changes
2. **Console**: Browser DevTools mein errors check karo
3. **Flask Logs**: Terminal mein requests logs dekhega

## 🚀 Deployment Ready

Production mein deploy karna ho to:
```bash
pip install gunicorn
gunicorn app:app
```

## 📧 Contact Form Setup

Contact form ko email bhej ne ke liye:
1. Flask-Mail install karo
2. Email credentials setup karo
3. `app.py` mein email configuration add karo

## 🎓 Learning Resources

- Flask: https://flask.palletsprojects.com/
- Bootstrap: https://getbootstrap.com/
- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript

## 📄 License

Personal use ke liye free hai

## 🙏 Thank You

Aapka portfolio application ready hai! Enjoy karo aur agar koi issue ho to fix kar sakte ho! 

**Happy Coding! 🚀**
