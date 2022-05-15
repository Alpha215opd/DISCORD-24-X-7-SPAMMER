from webserver import keep_alive
import requests

channelID = 975283941328183329
headers = {
    "authorization":
    "OTIzOTYxNjQyNjk2NDU0MTY1.GMo-mc.54VvvHY0yxbYpsxQ35559OJPUo3jc3L1rSP8Gw"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
