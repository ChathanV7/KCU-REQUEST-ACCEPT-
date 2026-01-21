import os
from flask import Flask
from threading import Thread

# Create a dummy Flask app for Render health checks
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is alive", 200

def run_server():
    # Render automatically provides the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Start the server in a separate thread so it doesn't block the bot
Thread(target=run_server, daemon=True).start()

# --- YOUR EXISTING BOT CODE START ---
# Example: client.run()
# --- YOUR EXISTING BOT CODE END ---

@app.route('/')
def hello_world():
    return 'TechVJ'


if __name__ == "__main__":
    app.run()
