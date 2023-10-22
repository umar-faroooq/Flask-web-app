from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "Location": "Islamabad, Pakistan",
        "Salary": "RS 15,00,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "Location": "Loss Angeles, USA",
        "Salary": "$ 150,000"
    },
    {
        "id": 3,
        "title": "Machine Learning Engineer",
        "Location": "Hybriid, Islamabad, Pakistan",
        "Salary": "RS 25,00,000"
    },
    {
        "id": 4,
        "title": "LLM Researcher",
        "Location": "Lahore, Punjab, Pakistan",
        # "Salary": "RS 35,00,000"
    },
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS, company_name="Nexoleaf")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__=="__main__":
    app.run(debug=True)


