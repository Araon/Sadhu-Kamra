import requests

url = "https://discord.com/api/webhooks/848514072194580511/_7RDKRz4PeX3oPPaRuPsA8P-3287J6uFoUAiXYtA0yygVPOdkLV3HphfLargI1dJ9eJi"

def notify(message):

    data = {
        "content": "Tweet Posted: "+message,

    }

    headers = {
        "Content-Type": "application/json"
    }

    result = requests.post(url, json=data, headers=headers)
    if 200 <= result.status_code < 300:
        print(f"Webhook sent {result.status_code}")
    else:
        print(f"Not sent with {result.status_code}, response:\n{result.json()}")
