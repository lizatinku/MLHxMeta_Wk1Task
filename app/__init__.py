import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('about.html', title="About Liza Tinku")

@app.route('/experience')
def experience():
    experiences = [
        {
            "title": "Production Engineering/SRE Fellow",
            "date": "June 2025 – Present",
            "ongoing": True,
            "description": "Selected for the Meta and MLH Fellowship which has a 2.5% acceptance rate. Working on impactful projects under the guidance of Meta mentors.",
        },
        {
            "title": "Undergraduate Researcher",
            "date": "Sept 2024 – Present",
            "ongoing": True,
            "description": "Building ML models to predict Alzheimer's progression. Presented work at Northern California Undergraduate Research Symposium at SJSU.",
        },
        {
            "title": "Full-stack Developer(Freelance)",
            "date": "Dec 2024 – March 2025",
            "ongoing": False,
            "description": "Built a website using the MERN stack for a landscaping business. Implemented REST APIs in backend & designed frontend in React.js",
        },
        {
            "title": "SWE at AI Student Collective(AISC)",
            "date": "Oct 2024 - May 2025",
            "ongoing": False,
            "description": "Led frontend development for an AI-powered ASL translator. Designed UI in Figma and built using Next.js and Tailwind CSS.",
        },
        {
            "title": "Computer Room Consultant at UC Davis IET",
            "date": "Sept 2024 - Dec 2024",
            "ongoing": False,
            "description": "Provided Mac/Windows troubleshooting support for 100+ faculty and students. Ensured compliance with UC Davis policies.",
        },
        {
            "title": "ML Engineer at GDSC Club",
            "date": "Nov 2022 – March 2023",
            "ongoing": False,
            "description": "lt a flight price predictor using Python libraries. Learned the ML pipeline and evaluated model using ROC curves.",
        },

    ]
    return render_template("experience.html", experiences=experiences)

@app.route('/hobbies')
def hobbies():
    return render_template("hobbies.html", title="Hobbies")

@app.route("/projects")
def projects():
    project_data = [
        {
            "title": "PartyPal - HackDavis25",
            "description": "College can be overwhelming — from classes to job hunts to social pressure. 1 in 5 students feel pressured to drink or use drugs at parties. That’s why we built PartyPal: a live, map-based app that helps students find safe, sober events and nearby resources like Narcan pickup spots, SafeRide, and ERs — all with real-time info.",
            "tags": ["ReactNative", "TailwindCSS", "Supabase", "Expo"],
            "image": "img/party.jpg",
            "github_link": "https://github.com/lizatinku/HackDavis25-PartyPal.git"
        },
        {
            "title": "F1 Race Predictor",
            "description": "A web app that predicts Formula 1 race outcomes using real-time qualifying data, circuit metadata, and driver history. Trained a Gradient Boosting model on the 2024 F1 season to forecast 2025 race results.",
            "tags": ["Flask", "FastF1 API", "React"],
            "image": "img/f1.jpg",
            "github_link": "https://github.com/lizatinku/AISC-spring25-f1predictor.git"
        },
        {
            "title": "Indian Food Trivia",
            "description": "An interactive quiz app that takes users on a flavorful journey through Indian cuisine, with questions based on user-selected categories.",
            "tags": ["NextJS","Typescript", "TailwindCSS"],
            "image": "img/indianfood.jpg",
            "demo_link": "food-trivia-deploy.vercel.app",
            "github_link": "https://github.com/lizatinku/food-trivia.git"
        },
        {
            "title": "Expense Tracker",
            "description": "Developed a website to simplify financial management for college students inspired by Notion's expense template and Bank of America's AI Erica.",
            "tags": ["React","Firebase", "FinnHub's API", "CSS"],
            "image": "img/money.avif",
            "demo_link": "expense-tracker-ashen-eta.vercel.app",
            "github_link": "https://github.com/lizatinku/expense-tracker.git"
        },
    ]
    return render_template("projects.html", projects=project_data)
