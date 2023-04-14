from flask import Flask, request, redirect, url_for, render_template
import requests
import config
import discord_helper

app = Flask(__name__)

@app.route("/")
def index():
    discord_auth_url = f"{config.AUTHORIZATION_BASE_URL}?client_id={config.CLIENT_ID}&redirect_uri={config.REDIRECT_URI}&response_type=code&scope={config.SCOPE}"
    return render_template("index.html", auth_url=discord_auth_url)

@app.route("/authorized")
def authorized():
    code = request.args.get("code")
    if not code:
        return "Error: code not found", 401

    data = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": config.REDIRECT_URI,
        "scope": config.SCOPE.replace("%20", " "),
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    token_response = requests.post(config.TOKEN_URL, data=data, headers=headers)
    token = token_response.json().get("access_token")

    # Call the Discord API
    user = discord_helper.get_user(token)
    guilds = discord_helper.get_guilds(token)
    # Iterate through all friends
    # Get history for all for 1 day
    # { "Sanjay": {}, "Matthew": {} }
    # history = 

    guild_channels = {}
    for guild in guilds:
        channels = discord_helper.get_channels(token, guild["id"])
        print(channels)
        guild_channels[guild["id"]] = channels


    insights = {
        "user": user,
        "guilds": guilds,
        "guild_channels": guild_channels,
    }
    return render_template("insights.html", insights=insights)

if __name__ == "__main__":
    app.run(debug=True)
