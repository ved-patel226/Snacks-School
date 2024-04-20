from flask import Flask, render_template
import requests


posts = requests.get("https://api.npoint.io/783f6c134b3269a4e293").json()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', all_posts = posts)

if __name__ == '__main__':
    app.run(debug=True)