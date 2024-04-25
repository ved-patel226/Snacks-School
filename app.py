from flask import Flask, render_template, request, jsonify
from discord_webhook import DiscordWebhook
import requests
import time
app = Flask(__name__)

# Load posts from the provided API endpoint
posts = requests.get("https://api.npoint.io/a3490619a628b4e0940a").json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the candy name from the request payload
        candy_name = request.json.get('candy_name')
        price_real = request.json.get('price_real')
        
        # Handle the form submission here
        # Replace 'WEBHOOK_URL_HERE' with your actual Discord webhook URL
        webhook_url = 'https://discord.com/api/webhooks/1232823457406910485/5-j04hyT8HjrYnQaQm0FhY-3dV67l3hUEjWxmdT5mPt9wkbebA2H0YJVblClBZ-vo0J1'
        content = f'Order Submitted for {candy_name} with price (teerth i quit price)!'
        webhook = DiscordWebhook(url=webhook_url, content=content)
        response = webhook.execute()
        return ''  # Return an empty response to the AJAX request
    else:
        return render_template('index.html', all_posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
