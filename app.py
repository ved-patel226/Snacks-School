from flask import Flask, render_template, request, jsonify, redirect, url_for
from discord_webhook import DiscordWebhook
import requests
import time
app = Flask(__name__)

# Load posts from the provided API endpoint
posts = requests.get("https://api.npoint.io/783f6c134b3269a4e293").json()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the candy name from the request payload
        candy_name = request.form['candy_name']
        person_name = request.form['person_name']
        candy_price = request.form['candy_price']
        # Handle the form submission here
        # Replace 'WEBHOOK_URL_HERE' with your actual Discord webhook URL
        webhook_url = 'https://discord.com/api/webhooks/1232823457406910485/5-j04hyT8HjrYnQaQm0FhY-3dV67l3hUEjWxmdT5mPt9wkbebA2H0YJVblClBZ-vo0J1'
        content = f'Order Submitted for {candy_name} by {person_name} they will pay you {candy_price} YAYYY MONNEY!'
        webhook = DiscordWebhook(url=webhook_url, content=content)
        response = webhook.execute()
        return render_template('index.html', all_posts=posts, success=True)
    else:
        return render_template('index.html', all_posts=posts, success=False)

@app.route('/order_submitted')
def order_submitted():
    print('dfsjaldkfasf')
    return render_template('order_submitted.html')


if __name__ == '__main__':
    app.run(debug=True)
