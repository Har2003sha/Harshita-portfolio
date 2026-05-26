from flask import Flask, render_template

app = Flask(__name__)

# =========================================================
# PROJECT DATA
# =========================================================

projects = [

    {
        'id': 1,

        'title': 'Heart Attack Prediction System',

        'description': 'Machine learning based healthcare prediction system for heart disease analysis.',

        'technologies': [
            'Python',
            'Flask',
            'Machine Learning',
            'Scikit-learn',
            'HTML',
            'CSS',
            'Bootstrap'
        ],

        'image': 'heart.jpg',

        'github': 'https://github.com/Har2003sha/heart-disease-prediction.git',

        'details': '''
This project predicts the chances of heart disease using machine learning algorithms based on patient medical records and health parameters.
        '''
    },

    {
        'id': 2,

        'title': 'Road Accident Analysis',

        'description': 'Interactive Power BI dashboard for road accident and casualty analysis.',

        'technologies': [
            'Power BI',
            'Excel',
            'DAX',
            'Data Analytics',
            'Dashboard Design'
        ],

        'image': 'road accident.jpg',

        'github': 'https://github.com/Har2003sha/Road-Accidents-Analysis.git',

        'details': '''
This Power BI dashboard analyzes road accident datasets to identify accident severity and casualty trends.
        '''
    },

    {
        'id': 3,

        'title': 'Crowd Management System',

        'description': 'YOLOv8 based real-time crowd detection and monitoring web application.',

        'technologies': [
            'Python',
            'YOLOv8',
            'OpenCV',
            'Flask',
            'Computer Vision',
            'HTML',
            'CSS',
            'JavaScript'
        ],

        'image': 'crowd.png',

        'github': 'https://github.com/Har2003sha/Crowd-Management-WebApp-Detect-Live-using-YOLO8.git',

        'details': '''
This AI-powered system detects and monitors crowds in real-time using YOLOv8 and OpenCV.
        '''
    }

]

# =========================================================
# ROUTES
# =========================================================

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html')


@app.route('/info')

def info():
    return render_template('info.html')


@app.route('/aboutme')

def aboutme():
    return render_template('aboutme.html')


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


@app.route('/contact')

def contact():
    return render_template('contact.html')


# =========================================================
# RUN APP
# =========================================================

if __name__ == '__main__':

    app.run(debug=True)