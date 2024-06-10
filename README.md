# Discord webhooks simplified for Python

Download DiscordWebhook.py & Install dependency:

```
pip install requests
```

## Create a webhook object

```python
# When initializing, the only required parameter is the webhook URL
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/example/1234", content="Hello world")

# Due to Discord's implementation, the message content or embeds must be set before executing
webhook.execute()
```

## Set values when initializing or after

```python
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/example/1234")

webhook.setContent("Hello World")

webhook.setUsername("John Doe")

# Execute multiple times
webhook.execute()
webhook.execute()
```

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

### Helpful Discord webhook documentation: https://birdie0.github.io/discord-webhooks-guide/index.html
