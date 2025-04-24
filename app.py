from flask import Flask, render_template
import requests


# Creating and initializing the app
app = Flask(__name__)


# The API function for newsAPI
def get_data():
    API_KEY = '01dac68f06ce480ea4af561660c3a3de'
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data

    return None



# The home function, rendering index.html
@app.route("/")
def home():
    data = get_data()
    return render_template("index.html", data=data)


@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
