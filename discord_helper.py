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
    headers = {"Authorization": f"Bot {token}"}
    response = requests.get(f"https://discord.com/api/v10/guilds/{guildId}/channels", headers=headers)
    return response.json()

def get_channel_history(token,channel_id):
    # /channels/{channel.id}/messages
    headers = {"Authorization": f"Bot {token}"}
    response = requests.get(f"https://discord.com/api/v10/channels/{channel_id}/messages", headers=headers)
    return response.json()
# [{'id': '761586559853658113', 'type': 4, 'name': 'Text Channels', 'position': 0, 'flags': 0, 'parent_id': None, 'guild_id': '761586559853658112', 'permission_overwrites': []}, {'id': '761586559853658114', 'type': 4, 'name': 'Voice Channels', 'position': 0, 'flags': 0, 'parent_id': None, 'guild_id': '761586559853658112', 'permission_overwrites': []}, {'id': '761586559853658115', 'last_message_id': '1019840995250143252', 'type': 0, 'name': 'general', 'position': 0, 'flags': 0, 'parent_id': '761586559853658113', 'topic': None, 'guild_id': '761586559853658112', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}, {'id': '761586559853658116', 'last_message_id': None, 'type': 2, 'name': 'General', 'position': 0, 'flags': 0, 'parent_id': '761586559853658114', 'bitrate': 64000, 'user_limit': 0, 'rtc_region': None, 'guild_id': '761586559853658112', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}, {'id': '761587408038789203', 'last_message_id': '955137310243049574', 'type': 0, 'name': 'music-spam', 'position': 1, 'flags': 0, 'parent_id': '761586559853658113', 'topic': None, 'guild_id': '761586559853658112', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}, {'id': '761824662853910528', 'last_message_id': '955137349199753256', 'type': 0, 'name': 'among-us', 'position': 2, 'flags': 0, 'parent_id': '761586559853658113', 'topic': None, 'guild_id': '761586559853658112', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}, {'id': '761829600635912212', 'last_message_id': None, 'type': 2, 'name': 'Brawlhalla', 'position': 1, 'flags': 0, 'parent_id': '761586559853658114', 'bitrate': 64000, 'user_limit': 0, 'rtc_region': None, 'guild_id': '761586559853658112', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}, {'id': '761829672123236382', 'last_message_id': None, 'type': 2, 'name': 'Valorant', 'position': 2, 'flags': 0, 'parent_id': '761586559853658114', 'bitrate': 64000, 'user_limit': 0, 'rtc_region': None, 'guild_id': '761586559853658112', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}, {'id': '889523142593241148', 'last_message_id': '997364940006502420', 'type': 0, 'name': 'bot', 'position': 3, 'flags': 0, 'parent_id': '761586559853658113', 'topic': None, 'guild_id': '761586559853658112', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}]

# def get_channel_history(token):
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
#     return response.json()

# def get_guild_members(token, guild_id):
#     print("Here")
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/members?limit=1000", headers=headers)
#     return response.json()
