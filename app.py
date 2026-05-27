from flask import Flask, render_template

app = Flask(__name__)

# =========================
# PROJECT DATA
# =========================

projects = [

    {
        "id": 1,

        "title": "Heart Attack Prediction System",

        "description":
        "Machine learning based healthcare prediction system.",

        "technologies": [
            "Python",
            "Flask",
            "Machine Learning",
            "Scikit-learn"
        ],

        "image": "heart.jpg",

        "github":
        "https://github.com/Har2003sha/heart-disease-prediction.git",

        "details":
        "Heart disease prediction using Machine Learning algorithms and Flask framework."
    },

    {
        "id": 2,

        "title": "Road Accident Analysis",

        "description":
        "Power BI dashboard for accident analysis.",

        "technologies": [
            "Power BI",
            "Excel",
            "DAX"
        ],

        "image": "road_accident.jpg",

        "github":
        "https://github.com/Har2003sha/Road-Accidents-Analysis.git",

        "details":
        "Road accident analysis dashboard using Power BI and Excel."
    },

    {
        "id": 3,

        "title": "Crowd Management System",

        "description":
        "YOLOv8 crowd detection project.",

        "technologies": [
            "Python",
            "YOLOv8",
            "OpenCV",
            "Flask"
        ],

        "image": "crowd.png",

        "github":
        "https://github.com/Har2003sha/Crowd-Management-WebApp-Detect-Live-using-YOLO8.git",

        "details":
        "AI based crowd monitoring and live detection system using YOLOv8."
    }

]

# =========================
# ROUTES
# =========================

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects_page():

    return render_template(
        'projects.html',
        projects=projects
    )


@app.route('/project/<int:project_id>')
def project_detail(project_id):

    project = next(
        (p for p in projects if p['id'] == project_id),
        None
    )

    if project:

        return render_template(
            'project_detail.html',
            project=project
        )

    return "Project Not Found", 404


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/info')
def info():
    return render_template('info.html')


# =========================
# RUN APP
# =========================

if __name__ == '__main__':
    app.run(debug=True)