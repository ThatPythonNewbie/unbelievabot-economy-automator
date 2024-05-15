import requests, json, random, time
from time import sleep

channel = input("Economy channel ID: ")
delay = int(input("Economy work delay for this server: "))
prefix = input("UnbelievaBot prefix for this server: ")
token = input("Token: ")

headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'es,es-ES;q=0.9,en-US;q=0.8,ru;q=0.7',
    'Authorization': token,
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'referer': f'https://discord.com/channels/{channel}',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9147 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
}

payload = {
    'mobile_network_type': 'unknown',
    'content': f'{prefix}work',
    'tts': False,
    'flags': 0,
}

while True:
    while True:
        response = requests.post(
            f"https://discord.com/api/v9/channels/{channel}/messages",
            headers=headers,
            json=payload
        )
        if not response.status_code == 429:
            break
        else:
            retry = response.headers["retry_after"]
            print(f"Rate limited! Retrying in {str(int(retry) + 0.1)} seconds...")
            time.sleep(int(response))
    print("Command invoke success. Waiting for delay...")
    time.sleep(delay)
