from methods import *
from flask import Flask,render_template,request


app = Flask ("JobSearch")

@app.route ("/")
def home():
    return render_template("home.html")

@app.route ("/search")
def search():
    keyword=request.args.get("keyword")
    jobs = get_jobs(keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs,length = len(jobs))

app.run("127.0.0.1", debug=True)

