# Discord webhooks simplified for Python

Install dependency:
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
webhook.addEmbed(EmbedBuilder()
           .setTitle("My Title")
           .setDescription("My Description")
           .setColor("11111")

webhook.execute()
```

### Helpful Discord webhook documentation: https://birdie0.github.io/discord-webhooks-guide/index.html

