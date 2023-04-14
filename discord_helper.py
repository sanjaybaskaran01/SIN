import requests

def get_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
    return response.json()

def get_guilds(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
    return response.json()

def get_channels(token,guildId):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"https://discord.com/api/v10/guilds/{guildId}/channels", headers=headers)
    return response.json()


# def get_channel_history(token):
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
#     return response.json()

# def get_guild_members(token, guild_id):
#     print("Here")
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/members?limit=1000", headers=headers)
#     return response.json()
