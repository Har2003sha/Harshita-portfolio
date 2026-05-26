# 🚀 QUICK START GUIDE

## Setup करने के लिए सिर्फ 3 Steps!

### Step 1️⃣: Dependencies Install करो
```bash
cd "d:\harshita portfolio\portfolio_app"
pip install -r requirements.txt
```

### Step 2️⃣: Images को सही जगह रखो
अपनी project images को यहाँ रखो:
```
d:\harshita portfolio\portfolio_app\static\images\
```

### Step 3️⃣: Application Run करो
```bash
python app.py
```

✅ Done! अब browser खोलो: **http://localhost:5000**

---

## 📸 Images Add करना

तुम्हारी images को `static/images/` folder में रखो:
- `project1.jfif`
- `project2.jfif`  
- `project3.jfif`

Images automatically show हो जाएंगी projects page पर!

---

## ⚙️ Configuration करना

### अपनी Information Add करो (app.py में):

```python
about_info = {
    'name': 'तुम्हारा नाम',
    'title': 'तुम्हारा Title',
    'bio': 'तुम्हारा परिचय',
    'skills': ['Skill1', 'Skill2'],
}
```

### अपनी Projects Add करो:

```python
projects = [
    {
        'id': 1,
        'title': 'Project का नाम',
        'description': 'Project का description',
        'technologies': ['Python', 'Flask'],
        'image': 'project1.jfif',
        'details': 'विस्तार से जानकारी'
    }
]
```

---

## 🎨 Colors Change करना

`static/css/style.css` में जाओ और edit करो:

```css
:root {
    --primary-color: #667eea;      /* Primary color */
    --warning-color: #ffc107;      /* Highlight color */
    --dark-color: #2d3436;         /* Dark background */
}
```

---

## 📱 Pages Overview

| Page | URL | क्या दिखता है |
|------|-----|------------|
| Home | `/` | Hero + Featured Projects |
| Info | `/info` | Professional Info |
| About | `/aboutme` | Personal Introduction |
| Projects | `/projects` | All Projects Grid |
| Project Detail | `/project/1` | Full Project Info |
| Contact | `/contact` | Contact Form |

---

## ✨ Features जो सब को पसंद आएंगे

✅ Mobile Responsive - Phone पर perfect दिखता है
✅ Smooth Animations - Fade, slide, hover effects
✅ Interactive Forms - Contact form fully working
✅ Modern Design - Latest Bootstrap 5
✅ Fast Loading - Optimized code
✅ SEO Friendly - Proper HTML structure

---

## 🐛 Common Issues & Solutions

### Issue: "Port already in use"
```python
# app.py में change करो:
app.run(debug=True, port=8000)
```

### Issue: Images नहीं दिखाई दे रहे
- Check करो कि images `static/images/` में हैं
- Image names सही हैं
- Browser cache clear करो (Ctrl+Shift+Del)

### Issue: CSS नहीं लोड हो रहा
```bash
# Browser cache clear करो:
Ctrl + F5
```

---

## 📧 Contact Form को Email भेजने के लिए

Later इसे email feature add कर सकते हो Flask-Mail से!

---

## 🎯 अगली Steps (Optional)

1. **Email भेजना** - Flask-Mail add करो
2. **Database** - SQLAlchemy से database add करो
3. **Comments** - Projects पर comments add करो
4. **Dark Mode** - Theme toggle add करो
5. **Admin Panel** - Content manage करने के लिए

---

## 💬 File Structure समझना

```
portfolio_app/
├── app.py                    ← Main Flask file (यहाँ data add करो)
├── templates/                ← HTML pages
│   ├── base.html            ← Navigation + Footer
│   ├── index.html           ← Home page
│   ├── projects.html        ← Projects listing
│   └── contact.html         ← Contact form
├── static/
│   ├── css/style.css        ← सब styling (Colors यहाँ change करो)
│   ├── js/main.js           ← Animations
│   └── images/              ← तुम्हारी images (project1.jfif etc)
└── requirements.txt         ← Dependencies
```

---

## 🎓 अब कोई और चीज़ add करना हो?

ये code clean है और easily customize कर सकते हो:

- Different colors add करो
- More sections add करो
- Database connect करो
- API integrate करो

---

## ✅ Checklist

- [ ] Flask install किया
- [ ] Images folder में रखी
- [ ] app.py में अपनी info add की
- [ ] `python app.py` run किया
- [ ] http://localhost:5000 खोला
- [ ] सब pages check किये

---

**अगर कोई confusion हो तो code comments को read करो! सब explain किया है!** 

Happy Coding! 🚀💻
