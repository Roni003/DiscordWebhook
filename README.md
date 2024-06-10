# Discord webhooks simplified for Python

Download DiscordWebhook.py & Install dependency:

```
pip install requests
```

## Create a webhook object

```python
from webhook import DiscordWebhook, EmbedBuilder

# When initializing, the only required parameter is the webhook URL
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/example/1234", content="Hello world")

# Due to Discord's implementation, the message content or embeds must be set before executing
webhook.execute()
```
![image](https://github.com/Roni003/DiscordWebhookPy/assets/61784529/5bbfbbaa-5d8d-4209-8f60-dfbef66a5cae)


## Set values when initializing or after

```python
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/example/1234")

webhook.setContent("Hello World")

webhook.setUsername("John Doe")

# Execute multiple times
webhook.execute()
webhook.execute()
```
![image](https://github.com/Roni003/DiscordWebhookPy/assets/61784529/d201d535-4390-4650-8f36-ea2c6efd00eb)


## Send embeds

```python
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/example/1234")

webhook.setContent("Sending embeds...")

# Add up to 10 embeds to each webhook
w.addEmbed(EmbedBuilder()
		   .setTitle("Embed Title")
		   .setColor("242424")
		   .setDescription("Add a description here")
		   .addField(name="Field 1", value="Value 1", inline=True)
		   .addField(name="Field 2", value="Value 2", inline=True)
		   .addField(name="Field 3", value="Value 3", inline=False)
		   .setAuthor(name="Roni", icon_url="https://avatars.githubusercontent.com/u/61784529?v=4"))

w.execute()
```
![image](https://github.com/Roni003/DiscordWebhookPy/assets/61784529/7285093a-779f-4494-aa93-c33c163e36df)

### Helpful Discord webhook documentation: https://birdie0.github.io/discord-webhooks-guide/index.html
