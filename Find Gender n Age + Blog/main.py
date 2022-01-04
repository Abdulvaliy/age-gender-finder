from flask import Flask, render_template
from datetime import datetime
from random import *
import requests

GENDERIZE_ENDPOINT = "https://api.genderize.io"
AGIFY_ENDPOINT = "https://api.agify.io"

now = datetime.now()
year = now.time().replace(microsecond=0)
app = Flask(__name__)


@app.route("/")
def home():
    current_year = now.year
    random_number = randint(1, 100)
    return render_template('index.html', year=current_year, rand=random_number, now_time=year)

@app.route("/guess/<name>")
def identifier(name):
    parmeters = {
        "name": name
    }

    response = requests.get(url=GENDERIZE_ENDPOINT, params=parmeters)
    response2 =requests.get(url=AGIFY_ENDPOINT, params=parmeters)
    response.raise_for_status()
    data = response.json()
    data2 = response2.json()
    gender = data["gender"]
    age = data2["age"]
    return render_template('identifier.html', name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/bd48f6889705c92fa8ad"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

