import requests, json, time

config = json.loads(open("settings.json", "r").read())

msg = input("Message: ")

while True:
	requests.post(config["webhook_url"], data={"content": msg, "avatar_url": "https://i.pinimg.com/236x/aa/22/c7/aa22c77fb778676fd5ed15aa5bb72cbd--hawk-eye-buggy.jpg", "username": "Thomas Shelby#9918"})
	time.sleep(config["delay"])